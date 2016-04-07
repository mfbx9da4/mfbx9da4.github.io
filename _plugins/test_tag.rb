module Jekyll
  # from http://www.createdbypete.com/articles/create-a-custom-liquid-tag-as-a-jekyll-plugin/
  class TestTag < Liquid::Tag
    def initialize(tag_name, url, tokens)
      super
      puts "here #{url}"
      @url = url.strip
    end

    def lookup(context, name)
      lookup = context
      name.split(".").each { |value| lookup = lookup[value] }
      lookup
    end

    def render(context)
      # page_url = "#{lookup(context, 'site.url')}#{lookup(context, @url)}"

      <<-MARKUP.strip
      <pre class="qrcode">
        hi there here is some text
        hi there here is some text
        hi there here is some text
        hi there here is some text
        #{@url}
      </pre>
      MARKUP
    end
  end

  Liquid::Template.register_tag('qr', TestTag)
end
