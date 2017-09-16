function fish_loadcolors --description 'load Xresources colors'
	for color in (xrdb -query -all | sed s/^\*.//g | grep '\#\([0-9]\|[a-z]\)\{6\}') ; 
		set id (echo $color | cut -d ":" -f1 | tr '[:lower:]' '[:upper:]') ; 
		set value (echo $color | cut -d ":" -f2 | sed -e 's/^[ \t]*//') ; 
		set -Ux "TERM_"$id $value ; 
	end
end

set fish_color_autosuggestion white
set fish_color_command green
set fish_color_end blue
set fish_color_error red
set fish_color_param yellow
set fish_color_quote magenta --bold
set fish_color_redirection cyan
set fish_color_comment magenta
set fish_color_cwd yellow
