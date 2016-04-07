module Jekyll
  class TestHookTag < Liquid::Tag
    Jekyll::Hooks.register :pages, :pre_render do |a,b|
      # code to call after Jekyll renders a post
      user_agent = a["user_agent"]
      @message = "Got something pages #{a.class.name}, #{b.class.name}"
      @hey = "asdf"
    end

    Jekyll::Hooks.register :site, :pre_render do |a,b|
      # code to call after Jekyll renders a post
      @message = "Got something site #{a.class.name}, #{b.class.name}"
      @@site_thing = "Got something site #{a},startb#{b}"
      @hey = "asdf"
    end

    def initialize(tag_name, url, tokens)
      super
      # @message = url
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
        some message
        #{@message}
        #{@hey}
      </pre>
      MARKUP
    end
  end
  Liquid::Template.register_tag('testhook', TestHookTag)
end
