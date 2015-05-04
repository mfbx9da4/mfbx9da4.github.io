# Here I am just concatenating all the files
# This would probably be cleaner with csvstack and csvgrep
# http://csvkit.readthedocs.org/en/0.9.1/tutorial/3_power_tools.html#csvstack-combining-subsets
echo "Data","Dependencia Origem","Historico","Data do Balancete","Numero do documento","Valor", > out/out.csv;
cat "$1"/*.csv | grep -v "Curto Prazo" | grep -v "S A L D O" | grep -v "Saldo Anterior" | grep -v "Data do Balancete" >> out/out.csv;

# Just encoding
iconv -f ISO-8859-1 out/out.csv -t ASCII//TRANSLIT -o out/out.csv;

# All transactions by date
csvcut -c 1,3,6 out/out.csv | csvsort -c 1 -r > out/all-transations-by-date.csv
csvcut -c 1,3,6 out/out.csv | csvlook > out/all-transations-by-date.txt
# All transactions by value
csvcut -c 1,3,6 out/out.csv | csvsort -c 3 -r > out/all-transations-by-value.csv


# Output to sqlite
# Will have to do a DROP TABLE out before importing to sql
sqlite3 -line extracts.db 'DROP TABLE out;'
csvsql --db sqlite:///extracts.db --insert out/out.csv

# Calculations
current_file="out/spent.csv"
echo "Date","Value", > $current_file
sqlite3 -line extracts.db 'SELECT Strftime("01/%m/%Y", `data`), sum(valor) FROM out WHERE  Valor < 0 GROUP BY Strftime("%m", `data`) ORDER BY date(data) DESC;' -csv >> $current_file
csvcut -c 1,2 $current_file | csvlook
echo 'Spent per month'
echo 'mean:' $(csvstat -c 2 --mean $current_file)
echo 'median:' $(csvstat -c 2 --median $current_file)
echo 'stdev:' $(csvstat -c 2 --stdev $current_file)
echo 'min:' $(csvstat -c 2 --min $current_file)
echo 'max:' $(csvstat -c 2 --max $current_file)
echo 'sum:' $(csvstat -c 2 --sum $current_file)
echo $(csvstat -c 2 --count $current_file)

echo ''

current_file="out/earned.csv"
echo "Date","Value", > $current_file
sqlite3 -line extracts.db 'SELECT Strftime("01/%m/%Y", `data`), sum(valor) FROM out WHERE  Valor > 0 GROUP BY Strftime("%m", `data`) ORDER BY date(data) DESC;' -csv >> $current_file
csvcut -c 1,2 $current_file | csvlook
echo 'Earned per month'
echo 'mean:' $(csvstat -c 2 --mean $current_file)
echo 'median:' $(csvstat -c 2 --median $current_file)
echo 'stdev:' $(csvstat -c 2 --stdev $current_file)
echo 'min:' $(csvstat -c 2 --min $current_file)
echo 'max:' $(csvstat -c 2 --max $current_file)
echo 'sum:' $(csvstat -c 2 --sum $current_file)
echo $(csvstat -c 2 --count $current_file)

echo ''

total_spent=$(sqlite3 -line extracts.db 'SELECT sum(valor) FROM out WHERE  Valor < 0;' -column);
total_earned=$(sqlite3 -line extracts.db 'SELECT sum(valor) FROM out WHERE  Valor > 0;' -column);
echo 'Total spent:' "$total_spent"
echo 'Total earned:' "$total_earned"

echo 'Balance:' `echo "${total_earned}" + "${total_spent}" | bc`;

echo ''

saved_per_month=$(echo $(csvstat -c 2 --mean out/earned.csv) + $(csvstat -c 2 --mean out/spent.csv)| bc);
saved_per_month_perc=$(echo $saved_per_month / $(csvstat -c 2 --mean out/earned.csv) | bc -l);
echo 'Average saved per month: R$' $saved_per_month, `echo "$saved_per_month_perc * 100" | bc -l` %


