# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define f = Character('Отец', color="#c8ffc8")
define mh = Character('Главный герой', color="#c8ffc8")
define talker = Character("", color="#c8ffc8")
define b = Character("Братан", color="#c8ffc8")

# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
image father_drifter = "images/father.png"
image main_character = "images/aneme_mc.png"
image syurprize = "images/bg/surprize.jpg"
image jdm = "images/bg/jdpzdc.jpg"
image plane = "images/bg/plane.jpg"
image bagazh = "images/bg/bagazh.jpg"
image brothers_car = "images/bg/brothers_car.jpg"
image brother = "images/brother.png"
image road = "images/bg/road.jpg"

label start:

    scene syurprize

    play music "audio/1stepisode.mp3"

    show main_character
    with dissolve
    mh "Пап, а куда мы едем?"
    hide main_character
    with dissolve
    show father_drifter
    with dissolve
    f "Сюрприз."
    talker "Лицо отца сияло от счастья."
    f "Мы почти приехали."
    talker "Тогда я и представить себе не мог, что этот день перевернет мою жизнь."
    f "Мы на месте"

    scene jdm
    play music "audio/penis-music.mp3"
    talker "Мне было всего 5 когда отец привел меня на фестиваль JDM."
    talker "Мы провели там весь день, а мне хотелось ещё и ещё."
    talker "Я влюбился в эту культуру."

    scene plane
    play music "audio/turbulentnost.mp3"
    talker "Звук турбулентности..."
    talker "Турбулентность резко вернула меня в реальность."
    talker "До конца полета оставалось пара часов и я уже видел знакомые места своей родной страны."
    talker "Прошло 6 лет с момента моего отъезда в Америку на обучение."
    talker "И вот я возвращаюсь домой."
    talker "Спустя 6 долгих лет я наконец возвращаюсь домой."

    show main_character
    with dissolve
    mh "Интересно как много изменилось за это время?"
    hide main_character
    with dissolve

    scene bagazh
    play music "audio/1stepisode.mp3"
    talker "Выйдя с самолета и забрав гараж, я остановился перед выходом."
    show main_character
    with dissolve
    mh "Ещё немного и я дома. Приеду и завалюсь спать, перелёт меня утомил."
    hide main_character
    with dissolve

    scene brothers_car
    talker "Выйдя из здания аэропорта я вижу своего младшего брата на парковке."
    show main_character
    with dissolve
    mh "Ну ты и вымахал, братишка. Я тебя не сразу и узнал."
    talker "Мое лицо сияло от счастья."
    hide main_character
    with dissolve
    show brother
    with dissolve
    b "А ты вообще не изменился, братец. Ну что, едем домой?"
    hide brother
    with dissolve
    show main_character
    with dissolve
    mh "На чем едем?"
    hide main_character
    with dissolve
    show brother
    with dissolve
    play music "audio/engine_noize_true.mp3"
    b "На моей."
    talker "Мы сели в жигуль и поехали домой."

    scene road
    play music "audio/db.mp3"
    talker "Мы ехали минут 30 как вдруг…"
    show brother
    with dissolve
    b "Надоело."
    talker "Я вопросительно посмотрел на него."
    play sound "audio/nyoooooooooooom.mp3"
    talker "И тут он прибавляет газ и дергает ручник, заходя в поворот боком."

    return
