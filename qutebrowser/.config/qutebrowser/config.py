config.load_autoconfig()

c.auto_save.session = True
c.content.blocking.enabled = True
c.content.javascript.enabled = True

c.downloads.position = 'bottom'
c.spellcheck.languages = ['en-US']
c.tabs.last_close = 'close'

# Vertical tab bar
c.tabs.position = 'left'
c.tabs.width = '10%'
c.tabs.max_width = -1

# Vertical monitor fit width
c.zoom.default = '75'

# Fonts
c.fonts.default_family = ['tewi', 'LiterationMono Nerd Font']
c.fonts.tabs.selected = '10pt default_family'
c.fonts.tabs.unselected = '10pt default_family'

# Colors
#css = 'css/gruvbox-all-sites.css'
#config.bind(',n', f'config-cycle content.user_stylesheets {css} ""')
config.source('gruvbox.py')
