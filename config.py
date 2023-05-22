from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "s",lazy.spawn("gnome-screenshot -a")),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),

            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

widget_defaults = dict(
        font = "FiraCode Nerd Font Bold",
        fontsize = 11,
        padding = 8,)

args = {
        "border_focus":'FFD95A',
        "border_normal":'000000',
        "border_width":1,
        "margin":18,
        }

layouts = [
    layout.Columns(**args),
    layout.Max(**args),
    layout.Bsp(**args),
    layout.MonadTall(**args),
    layout.MonadWide(**args),
    layout.Tile(**args),
]

colors = ["1e2120","262b2a","303635","3a403f","262b2a",'5f6763',"525a57",'989b97','adafac','cbcdcb']
black = '1e2120'
white = '9b9e9a'
backgroundColor = '1f2322'

powerline = {"decorations": [PowerLineDecoration(path='arrow_right')]}
powerlineLeft = {"decorations": [PowerLineDecoration(path='arrow_left')]}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Clock(
                    format = '%I:%M %d/%m/%y',
                    fontsize = 14,
                    foreground = black,
                    background= colors[7], 
                    **powerlineLeft
                    ),

                widget.GroupBox(
                    highlight_method = 'line',
                    highlight_color = colors[7],
                    background = colors[8],
                    active = colors[4],
                    **powerlineLeft,
                    fontsize = 14
                    ),

                widget.Prompt(
                    foreground = black,
                    background = colors[9],
                    **powerlineLeft
                    ),

                widget.Spacer(**powerline),

                widget.OpenWeather(
                    location = "Coimbatore",
                    format = '{weather_details}',
                    update_interval = 1,
                    background = colors[5],
                    foreground = white,
                    **powerline
                    ),

               widget.CurrentLayout(
                    foreground = white,
                    background = colors[6],
                    **powerline
                    ),

               widget.CheckUpdates(
                       distro='Arch', 
                       no_update_string = 'No Updates',
                       display_format = '{updates}',
                       foreground = white,
                       background = colors[4],
                       **powerline
                       ),
 
               widget.CPU(
                       format = '{load_percent}%',
                       foreground = white,
                       background = colors[3],
                       **powerline
                       ),

               widget.Memory(
                       format = '{MemUsed: .0f}{mm}',
                       background = colors[2],
                       foreground = white,
                       **powerline
                       ),
 
               widget.Net(
                       format = '{down} ↓↑ {up}',
                       foreground = white,
                       background = colors[1],
                       **powerline
                       ),

               widget.Volume(
                      foreground = white,
                      background = colors[0]
                       ),
            ],
            24,
            background = backgroundColor,
            margin = 5,
        ),
    ),
]

follow_mouse_focus = False
auto_fullscreen = True
wmname = "LG3D"
