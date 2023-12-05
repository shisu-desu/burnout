## Данный файл содержит настройки, способные изменить вашу игру.
##
## Строки, начинающиеся  с двух '#' — комментарии, и вы не должны их
## раскомментировать. Строки, начинающиеся с одной '#' — комментированный код,
## который вы можете раскомментировать, если посчитаете это нужным.


## Основное ####################################################################


# Определение персонажей игры.
define f = Character('Отец', color="#ff5c68")
define mc = Character('Главный герой', color="#e5a377")
define talker = Character("???", color="#a2a2a2")
define b = Character("Братан", color="#72b651")
define m = Character("Мама", color="#a972fb")
define g = Character("Дед", color="#bdbe62")

#персонажи за мобилой

define mc_nvl = Character('Главный герой', kind=nvl, callback=Phone_SendSound)
define b_nvl = Character('Брат', kind=nvl, callback=Phone_ReceiveSound)

#   «  »

# music

define daylight = "audio/Daylight.mp3"
define air_guitar = "audio/Air Guitar.mp3"
define raindrops = "audio/Raindrops and Puddles.mp3"
define afternoon = "audio/Afternoon.mp3"
define citydrive = "audio/CityDrive.mp3"
define drift = "audio/Drift.mp3"
define broom = "audio/broom.mp3"


# задники
image white = "#ffffff"
image opening_dad = "images/bg/op_inacar.png"
image airport_outside = im.FactorScale("images/bg/airport_outside.png", 1.5)
image airport = "images/bg/airport.png"
image gasstation = im.FactorScale("images/bg/gasstation.png", 2.0)
image gasstation_night = im.FactorScale("images/bg/gasstation_night.png", 2.0)
image house_dining = im.FactorScale("images/bg/house_dining.jpg", 2.0)
image house_ent = im.FactorScale("images/bg/house_ent.jpg", 2.0)
image house_ext = im.FactorScale("images/bg/house_ext.jpg", 2.0)
image house_kitchen = im.FactorScale("images/bg/house_kitchen.jpg", 2.0)
image house_living = im.FactorScale("images/bg/house_living.jpg", 2.0)
image inside_86 = im.FactorScale("images/bg/inside_86.png", 1.8)
image jdm = im.FactorScale("images/bg/jdm.png", 1.2)
image jdm2 = "images/bg/jdm2.png"
image plane = "images/bg/plane.png"
image mountain = "images/bg/mountains.jpg"

# определение настроек

define long_fade = Fade(1.0, 0.0, 1.0)
define appearedfromright = ComposeTransition(dissolve, before=moveinright)
transform normal_right:
    xalign 0.8
    yalign 1.0
transform normal_left:
    xalign 0.2
    yalign 1.0
transform left:
    xalign 0.15
    yalign 1.0
transform right:
    xalign 0.85
    yalign 1.0


define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#персонажи
image mom = "images/chars/mom.png"
image dad = "images/chars/dad.png"
image grandpa = "images/chars/grandpa.png"
image brother = "images/chars/brother.png"


## Читаемое название игры. Используется при установке стандартного заголовка
## окна, показывается в интерфейсе и отчётах об ошибках.
##
## Символы "_()", окружающие название, отмечают его как пригодное для перевода.

define config.name = _("Burnout")


## Определяет, показывать ли заголовок, данный выше, на экране главного меню.
## Установите на False, чтобы спрятать заголовок.

define gui.show_name = True


## Версия игры.

define config.version = "0.3"


## Текст, помещённый в экран "Об игре". Поместите текст между тройными скобками.
## Для отделения абзацев оставляйте между ними пустую строку.

define gui.about = _p("""
""")


## Короткое название игры, используемое для исполняемых файлов и директорий при
## постройке дистрибутивов. Оно должно содержать текст формата ASCII и не должно
## содержать пробелы, двоеточия и точки с запятой.

define build.name = "Burnout"


## Звуки и музыка ##############################################################

## Эти три переменные управляют, среди прочего, тем, какие микшеры показываются
## игроку по умолчанию. Установка одной из них в False скроет соответствующий
## микшер.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## Чтобы разрешить игроку тестировать громкость на звуковом или голосовом
## каналах, раскомментируйте строчку и настройте пример звука для прослушивания.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Раскомментируйте следующую строчку, чтобы настроить аудиофайл, который будет
## проигрываться в главном меню. Этот файл продолжит проигрываться во время
## игры, если не будет остановлен, или не начнёт проигрываться другой аудиофайл.

define config.main_menu_music = "audio/mainmenu.mp3"


## Переходы ####################################################################
##
## Эти переменные задают переходы, используемые в различных событиях. Каждая
## переменная должна задавать переход или None, чтобы указать на то, что переход
## не должен использоваться.

## Вход и выход в игровое меню.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Переход между экранами игрового меню.

define config.intra_transition = dissolve


## Переход, используемый после загрузки слота сохранения.

define config.after_load_transition = None


## Используется при входе в главное меню после того, как игра закончится.

define config.end_game_transition = None


## Переменная, устанавливающая переход, когда старт игры не существует. Вместо
## неё используйте функцию with после показа начальной сценки.


## Управление окнами ###########################################################
##
## Эта строка контролирует, когда появляется диалоговое окно. Если "show" — оно
## всегда показано. Если "hide" — оно показывается, только когда представлен
## диалог. Если "auto" — окно скрыто до появления оператора scene и показывается
## при появлении диалога.
##
## После начала игры этот параметр можно изменить с помощью "window show",
## "window hide" и "window auto".

define config.window = "auto"


## Переходы, используемые при показе и скрытии диалогового окна

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Стандартные настройки #######################################################

## Контролирует стандартную скорость текста. По умолчанию, это 0 — мгновенно,
## в то время как любая другая цифра — это количество символов, печатаемых в
## секунду.

default preferences.text_cps = 80


## Стандартная задержка авточтения. Большие значения означают долгие ожидания, а
## от 0 до 30 — вполне допустимый диапазон.

default preferences.afm_time = 15


## Директория сохранений #######################################################
##
## Контролирует зависимое от платформы место, куда Ren'Py будет складывать файлы
## сохранения этой игры. Файлы сохранений будут храниться в:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>.
##
## Этот параметр обычно не должен изменяться, а если и изменился, должен быть
## текстовой строчкой, а не выражением.

define config.save_directory = "Vendetta-1695811464"


## Иконка ######################################################################
##
## Иконка, показываемая на панели задач или на dock.

define config.window_icon = "icon.png"


## Настройка Дистрибутива ######################################################
##
## Эта секция контролирует, как Ren'Py строит дистрибутивные файлы из вашего
## проекта.

init python:

    ## Следующие функции берут образцы файлов. Образцы файлов не учитывают
    ## регистр и соответствующе зависят от директории проекта (base), с или без
    ## учёта /, задающей директорию. Если обнаруживается множество одноимённых
    ## файлов, то используется только первый.
    ##
    ## Инструкция:
    ##
    ## / — разделитель директорий.
    ##
    ## * включает в себя все символы, исключая разделитель директорий.
    ##
    ## ** включает в себя все символы, включая разделитель директорий.
    ##
    ## Например, "*.txt" берёт все файлы формата txt из директории base, "game/
    ## **.ogg" берёт все файлы ogg из директории game и всех поддиректорий, а
    ## "**.psd" берёт все файлы psd из любого места проекта.

    ## Классифицируйте файлы как None, чтобы исключить их из дистрибутивов.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Чтобы архивировать файлы, классифицируйте их, например, как 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Файлы, соответствующие образцам документации, дублируются в приложениях
    ## Mac, чтобы они появлялись и в приложении, и в zip архиве.

    build.documentation('*.html')
    build.documentation('*.txt')


## Для совершения покупок в приложении требуется лицензионный ключ Google Play.
## Его можно найти в консоли разработчика Google Play в разделе "Монетизация" >
## "Настройка монетизации" > "Лицензирование".

# define build.google_play_key = "..."


## Имя пользователя и название проекта, ассоциированные с проектом на itch.io,
## разделённые дробью.

# define build.itch_project = "renpytom/test-project"
