package main

import "fmt"

func sumToN(n int) {
	return (n + 1) * n / 2
}

func substrCount(n int32, str string) int {
	count := 0
	i := 0
	for i < len(str) {
		let := str[i]
		start := i
		i++
		curCount := 1
		if i == len(str) {
			count++
			break
		}
		// leading up to middle element
		for i < len(str) && str[i] == let {
			curCount = sumToN(i + 1 - start)
			i++
		}
		// now on middle element
		j := i + 1
		size := 1
		// add pallindromes after middle element
		for j < len(str) && str[j] == let && j-i <= i-start {
			size = j - i
			curCount++
			j++
		}
		count += curCount
	}
	return count
}

func main() {
	fmt.Println("ans:", substrCount(4, "aaaa"))
}
