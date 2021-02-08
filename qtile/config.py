# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "termite" # guess_terminal()
COORDS = {"latitude": 39.961178, "longitude": -82.998795}

keys = [
    # ESSENTIAL BINDS #

    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
        ),
    Key([mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"
        ),
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
        ),
    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart qtile"
        ),
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown qtile"
        ),
    Key([mod, "shift"], "Return",
        lazy.spawn("rofi -modi drun -show drun -show-icons"),
        desc="Spawn a command using a prompt widget"
        ),

    # KEYBINDS FOR APPLICATIONS #

    Key([mod, "shift"], "b",
        lazy.spawn("firefox"),
        desc="Open firefox"
        ),
    Key([mod, "shift"], "d",
        lazy.spawn("discord"),
        desc="Open Discord"
        ),
    Key([mod], "Print",
        lazy.spawn("flameshot gui"),
        desc="Take a screenshot of a desired region using Flameshot"
        ),
    Key([mod, "control"], "Print",
        lazy.spawn("flameshot full -c"),
        desc="Take a screenshot of the entire screen using Flameshot"
        ),
    Key([mod, "shift"], "Print",
        lazy.spawn("flameshot full -c -p /home/pinwheel/Pictures/Screenshots"),
        desc="Take a screenshot of the entire screen and save to Screenshots folder."
        ),

    # WINDOW BINDS # ( First two are for MonadTall )
    Key([mod, "control"], "g",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "g",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "control"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),

    # Switch between windows in current stack pane

    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down in stack pane"
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up in stack pane"
        ),
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus left in stack pane"
        ),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus right in stack pane"
        ),

    # Move windows up or down in current stack

    Key([mod, "control"], "k",
        lazy.layout.shuffle_down(),
        desc="Move window down in current stack "
        ),
    Key([mod, "control"], "j",
        lazy.layout.shuffle_up(),
        desc="Move window up in current stack "
        ),
    Key([mod, "control"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window left in current stack "
        ),
    Key([mod, "control"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window right in current stack "
        ),

    # Grow windows #
    Key([mod, "mod1"], "j",
         lazy.layout.grow_down(),
         desc="Shrinks the window downwards",
         ),
    Key([mod, "mod1"], "k",
         lazy.layout.grow_up(),
         desc="Shrinks the window upwards",
         ),
    Key([mod, "mod1"], "h",
         lazy.layout.grow_left(),
         desc="Shrinks the window left",
         ),
    Key([mod, "mod1"], "l",
         lazy.layout.grow_right(),
         desc="Shrinks the window right",
         ),
]

# SET UP GROUPS #

group_names = [("1", {'layout': 'monadtall'}),
               ("2", {'layout': 'monadtall'}),
               ("3", {'layout': 'monadtall'}),
               ("4", {'layout': 'monadtall'}),
               ("5", {'layout': 'monadtall'}),
               ("6", {'layout': 'monadtall'}),
               ("7", {'layout': 'monadtall'}),
               ("8", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.extend([
        Key([mod], str(i), lazy.group[name].toscreen()), # Switch to certain group
        Key([mod, "shift"], str(i), lazy.window.togroup(name)), # Move window to group
        Key(["control", "shift"], str(i), lazy.window.togroup(name), lazy.group[name].toscreen()), # Move window to group and switch to that group
    ])

# GENERAL LAYOUT THEMING "

layout_theme = {
    "border_focus": "88c0d0", # d48ffc
    "border_normal": "81a1c1", # 903ac1
    "border_width": 4,
    "margin": 12,
    }


layouts = [
    # layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2, **layout_theme),
    # Try more layouts by unleashing below layouts.
    layout.Bsp(**layout_theme),
    # layout.Columns(**layout_theme),
    # layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.Floating(**layout_theme),
]

widget_defaults = dict(
    font='apercu mono',
    fontsize=18,
    padding=20,
)
extension_defaults = widget_defaults.copy()

colors = {
    "bg": "2e3440", # 2b303b
    "fg": "d8dee9", # c0c5ce
    "ic": "8fbcbb", # 8dfc74
    "ac": "bf616a", # 31f704
    "hl": "bf616a", # f902c8
    "bd": "88c0d0", # 02f97e
    "ubd": "b48ead", # ac35b7
    }


def get_screens():
    screens = [
        Screen(
            top=bar.Bar(
                [
                    widget.Image(
                        background=colors['bg'],
                        margin=3,
                        filename='~/Pictures/archicon.png',
                        mouse_callbacks = {"Button1": lambda qtile: qtile.cmd_spawn("firefox https://youtube.com")}
                    ),
                    widget.GroupBox(
                        highlight_method="block",
                        this_current_screen_border=colors['bd'],
                        urgent_border=colors['ubd'],
                        active=colors['ac'],
                        inactive=colors['ic'],
                        block_highlight_text_color=colors['hl'],
                        disable_drag=True,
                        background=colors['bg'],
                        foreground=colors['fg'],
                        borderwidth=3,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 3,
                        rounded=False
                    ),
                    widget.CurrentLayout(
                        background=colors['bg'],
                        foreground=colors['ic'],
                    ),
                    widget.WindowName(
                        background=colors['bg'],
                        foreground=colors['ic'],
                        fontsize=15,
                    ),
                    # widget.Sep(
                    #     background=colors['bg'],
                    #     foreground=colors['ic'],
                    #     linewidth=3,
                    #     padding=20
                    # ),
                    # widget.Image(
                    #     background=colors['bg'],
                    #     margin=3,
                    #     filename='~/Pictures/notebook.png',
                    #     mouse_callbacks = {"Button1": lambda qtile: qtile.cmd_spawn(f"notes.py")}
                    # ),
                    # widget.Sep(
                    #     background=colors['bg'],
                    #     foreground=colors['ic'],
                    #     linewidth=3,
                    #     padding=20
                    # ),
                    widget.Systray(
                        background=colors['bg'],
                        padding=20,
                    ),
                    widget.Sep(
                        background=colors['bg'],
                        foreground=colors['ic'],
                        linewidth=3,
                        padding=20
                    ),
                    widget.Clock(
                        background=colors['bg'],
                        foreground=colors['ic'],
                        format='%A, %B %d [ %H:%M ]',
                    ),
                ],
                opacity=0.8,
                size=30,
            ),
        ),
    ]
    return screens


if __name__ in ["config", "__main__"]:
    screens = get_screens()


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
