﻿label start:

    scene black 
    play music "audio/Terraria.mp3"

    "Да-да. Конечно. Супер, ждём все реквизиты на почту. И вам хорошего вечера."
    mc "Здравствуйте. В течение пары часов ждите реквизиты клиента на почте. Да, заявление у Вас на столе. Рад был с Вами работать. Спасибо, и Вам хорошего вечера."
    "Наконец-то. Это была самая сложная сделка в моей жизни."
    "Как же она меня вымотала."
    "Я сделал глубокий выдох, потянулся, откинул спинку кресла и задремал."

    scene white with long_fade

    scene opening_dad with dissolve
    mc "Пап, а куда мы едем?"

    f "Сюрприз."
    "Лицо отца сияло от счастья."
    f "Мы почти приехали."
    "Тогда я и представить себе не мог, что этот день перевернет мою жизнь."
    f "Мы на месте"

    scene jdm with fade
    play music "audio/penis-music.mp3"
    "Мне было всего 5 когда отец привел меня на фестиваль JDM."
    "Мы провели там весь день, а мне хотелось ещё и ещё."
    "Я влюбился в эту культуру."
    "Повсюду был лязг шин, куча дыма и рев моторов."
    play music "audio/turbulentnost.mp3"
    scene white with long_fade
    scene plane with dissolve
    "Звук турбулентности..."
    "Турбулентность резко вернула меня в реальность."
    "До конца полета оставалось пара часов и я уже видел знакомые места своей родной страны."
    "Прошло 6 лет с момента моего отъезда в Америку на обучение."
    "И вот я возвращаюсь домой."
    "Спустя 6 долгих лет я наконец возвращаюсь домой."
    stop music fadeout 2.0
    mc "Интересно как много изменилось за это время?"
     

    scene airport with long_fade
    play music air_guitar
    "Выйдя с самолета и забрав гараж, я остановился перед выходом."
    mc "Ещё немного и я дома."

    b_nvl "Здарова, братан, как житуха?"
    mc_nvl "Нормас бро сам как ваще где тя искать"
    nvl_narrator "1xbet"
    nvl_narrator "1xbet"
    nvl_narrator "1xbet"
    nvl clear

    mc "Приеду и завалюсь спать, перелёт меня утомил." 
    
    nvl show
    pause 2.0
    

    scene airport_outside
    "Выйдя из здания аэропорта я вижу своего младшего брата на парковке."

    mc "Ну ты и вымахал, братишка. Я тебя не сразу и узнал."
    "Мое лицо сияло от счастья."
    
    show brother 
    with dissolve
    b "А ты вообще не изменился, братец. Ну что, едем домой?"
    mc "На чем едем?"
    play music "audio/engine_noize_true.mp3"
    b "На моей."

    hide brother with dissolve 
    scene black with fade

    scene inside_86 with long_fade # поменять бг
    play music citydrive
    mc "Откуда у тебя столько денег на такую машину?"
    b "Мы с отцом собирали ее по запчастям. На удивление вышло дешевле, чем кажется."
    mc "Сколько девчонок успел запикапить?"
    b "Очень смешно."
    "Мы начали ускоряться, а на спидометре уже перевалило за 150 километров в час."
    "Я вопросительно посмотрел на него."
    scene black with fade # бг дрифта
    play sound drift
    "И тут он дергает ручник, заходя в поворот боком."
    scene inside_86 with long_fade
    mc "Не знал что ты любитель подрифтить"
    "Сказал я в неком экстазе и небольшой дрожью в голосе."
    b "Много чего изменилось за 6 лет."
    "Сказал брат с некой гордостью и улыбнулся"

    
    scene gasstation with fade
    play music daylight
    "Брат свернул на до боли знакомую заправку."
    "Это была заправка №10." 
    "Заправка нашего дедушки."
    mc "Как же долго я её не видел."
    talker "Поменяйте масло пожалуйста."
    talker "Сколько с меня?"
    "Меня сразу накрыли воспоминания как я маленький сидел на этой заправке с дедушкой и ждал пока отец закончит работать в мастерской."
    "Каждый раз я умудрялся учудить что-то новое."
    "То обвалить полку в магазине при заправке, то масло разлить, рассыпать все гайки в мастерской отца."
    "А испачкаться для меня было отдельным видом искусства."
    "Взглянув в давно не мытое окно мастерской я увидел семилетнего себя."
    b "Ну что, едем?"
    show brother with dissolve
    "Голос брата вывел меня из ностальгии."
    
    mc "Давно пора. Я слишком долго не был дома. Хочу поскорее всех увидеть."

    scene inside_86 with long_fade
    "Оставшаяся дорога прошла в молчании." 
    "Лишь изредка брат наваливал боком, показывая своё мастерство."

    scene house_ext with fade
    show brother with dissolve
    b "Вот мы и дома."
    "Брат нарушил тишину и вывел меня из залипания в окно."
    "Я и забыл как здесь красиво."

    scene house_ent with fade
    b "Как думаешь, мы успели к ужину?"
    "Спросил меня братец потягиваясь от долгой поездки."
    "Мы и правда ехали долго, начало смеркаться."
    
    scene house_living
    show mom with moveinleft
    m "С возвращением!"
    show mom with dissolve:
        zoom 2.0
        yalign 0.1
    "С радостью и слезами на глазах сжимала меня в объятиях мама."
    show mom with dissolve:
        zoom 1.0
        yalign 1.0
    talker "Добро пожаловать домой."
    show mom at normal_right with move
    show dad at normal_left with moveinleft
    "С неким облегчением в голосе сказал отец, выйдя из гостинной."
    mc "А чем так вкусно пахнет?"
    "Улыбаясь до ушей и внюхиваясь спросил я."
    m "Увидишь."
    "Немного дразня моё любопытство сказала мама."

    scene house_kitchen with dissolve
    mc "Как вкусно пахнет."
    scene house_kitchen with hpunch
    show dad with dissolve
    f "Куда?"
    "Одёрнул отец, заметив мои намерения."
    f "Ещё не все пришли."
    show dad at normal_right with move
    show brother at normal_left with dissolve
    b "Я могу не удержаться."
    "Сказал он опять намереваясь что-нибудь стащить со стола."

    scene house_dining 
    show dad at normal_right
    show brother at normal_left
    with dissolve
    f "Лучше расскажи как прошло обучение? Как работа?"
    "И правда, я ведь ничего им не рассказывал пока учился, а из-за работы у меня почти не было свободного времени. Мы очень редко созванивались."
    scene black with dissolve
    "И я начал свой рассказ с воодушевлением, стараясь не упустить ни малейшей детали."
    scene house_dining
    show dad at normal_right 
    show brother at normal_left
    with dissolve
    f "Это была воистину сделка века, сынок."
    "Сказал отец, гордясь достижениями сына."
    f "А с девушками как? Нашел кого нибудь?"
    stop music fadeout 7.0
    "Этот вопрос ввёл меня в небольшую грусть."
    mc "Нет, девушку я себе так и не нашел..." 
    mc "Была одна, но она была не больше чем просто друг."
    show dad at right
    show brother at left 
    with move 
    show mom with dissolve
    m "Не расстраивайся, родной. Найдешь ещё вторую половинку."
    "Сказала мама, стараясь меня утешить."
    "Дабы хоть как-то вывести разговор с неловкой паузы отец спросил..."
    f "Надеюсь ты все также любишь машины?"
    mc "Только сильнее. Я даже освоил фотошоп, чтобы сделать несколько своих проектов."
    f "Обязательно мне потом покажи."
    mc "Обещаю."
    talker "Простите за опоздание."
    "Я услышал очень знакомый голос."
    "Моя душа словно вернулась лет на 10 назад."
    "Это был мой лучший друг, с которым мы крепко дружили ещё с младших классов."
    show brother:
        xalign 0.1
    show mom:
        xalign 0.3
    show dad:
        xalign 0.55
    with move
    show grandpa at right
    with dissolve
    g "С приездом, внучок!"
    "Чувство счастья накрыло мне с головой."
    "Я дома."
    "Все было так же, как и до моего отъезда учиться."
    "Словно и не было этих 6 лет."
    play music raindrops
    "Мы сидели за столом и разговаривали обо всем."
    m "Cынок, ты же сдал на права?"
    mc "Да. Первый год был не сложным и я смогу и на права сдать, и сессию на «отлично» сдать."
    f "Думал уже о своей первой машине?"
    mc "Задумывался пару раз, но ничего конкретного не выбрал."
    f "Мне просто нужна твоя помощь в мастерской."
    g "Заодно и на заправке мне поможешь."
    "Улыбаясь сказал дед"
    b "Я решил повторить за братом и тоже поступил. Но не за границу, а в соседнем городе."
    g "Раз уж такое дело, можешь взять мою {color=#f00}{b}{i}ХАЧИРОКУ{/i}{/color}."
    if not persistent.dict1_unlock:
        $ persistent.dict1_unlock = True
        play sound broom
        call screen guide("Теперь вам открыт словарь!")
        call screen guide("Проверь меню игры!")
    "Дедушка протянул мне ключи от машины."
    g "Она все равно стоит."
    "Я не верил своим глазам и ушам."
    mc "Правда?"
    g "Я тебя хоть раз обманывал?"
    "Дедушка был полон счастья."
    mc "Загибай пальцы."
    "Он подготовил руки, чтобы считать."
    g "Ладно-ладно, было пару раз."
    "Все сидевшие за столом дружно засмеялись."
    "Дедушка любил надо мной подшутить. Я иногда обижался, но быстро отходил."
    "И только сейчас я понял, что не смотря на тяжёлые времена, мы прожили их весело и счастливо."
    g "Сейчас я полностью серьёзен. Я уже староват ездить на ней. Уж лучше ты меня проводишь."
    "Я и не заметил как мои глаза наполнились слезами. С этой машиной у меня связано много счастливых воспоминаний." 
    "Она считалась членом семьи."
    g "Береги её."
    mc "Обязательно."
    stop music fadeout 5.0

    scene black with dissolve
    "Я и не заметил, что на часах было уже 4 утра."
    "Все разошлись спать."
    "Несмотря на усталость после перелета заснул я не сразу."
    "В голове крутился всего один вопрос..."
    "Что же будет дальше?"

    scene house_living with dissolve
    "Проснулся я на удивление в девять утра и чувствовал себя отдохнувшим."
    "Отец с дедом ждали меня, чтобы отправляться на работу."
    scene house_dining with dissolve
    "Выпив горячего чая и взяв бэнто, мы сели к брату в машину и поехали в мастерскую."
    scene black with dissolve
    "Ехали мы в тишине."

    scene gasstation 
    show dad
    with dissolve
    play music afternoon
    "По приезду на место мы с отцом пошли в гараж, который стоял за мастерской."
    "Гараж был просто завален деталями. И не смотря на его размеры, в нем было довольно тесновато, но отцу для работы места хватало."
    "Весь гараж был заставлен ящиками, стеллажами, повсюду лежали детали."
    "АЕ86 моего деда стояла в дальнем углу гаража под тентом."
    f "Ну что, давай её оттуда вытащим?"
    "Мы с отцом провозились за ее «освобождением» до самого обеда."
    "Выкатив ее из гаража я снял тент."
    "Хачи была вся в пыли. Не верилось, что она вообще сможет завестись."
    "Проверив все жидкости Отец сказал мне попробовать ее завести."
    "{i}Звук мотора{/i}"
    show dad at left with move 
    show grandpa at right with dissolve
    g "Есть ещё порох!"
    "Вдруг воскликнул дед."
    "Я и сам был очень удивлен."
    "Столько лет она стояла в гараже, столько лет за ней не следили, а она все равно заводится."
    g "Прокатись-ка."
    "Я сначала не понял, что это было адресовано мне."
    "Минуты две я стоял и смотрел на нее."  
    scene black with dissolve
    "Сделав круг вокруг заправки, Я вернулся обратно."
    "Пока я на ней катался, Я заметил, что она немного отличается от машин, на которых я ездил."
    show gasstation with dissolve
    show grandpa with dissolve
    g "Ну как она тебе?"
    mc "Она просто нечто. Спасибо, дедушка."
    g "Пусть она послужит тебе так же, как служила мне."
    hide grandpa with dissolve
    "Мы сидели перед бензоколонкой и обедали."
    "Работы как факт не было, все разъехались."
    scene gasstation with pushup
    "Отец показал мне свой гараж и объяснил какая помощь ему там нужна. Звучит просто."
    scene gasstation with pushup
    "Потом дедушка рассказал чем ему нужно помочь на заправке. Ничего сложного."
    scene gasstation with pushup
    "Остаток дня мы провели в работе."
    "Я то выполнял поручения отца в мастерской, то заправлял машины."
    scene gasstation_night with Dissolve(3.5)
    show dad with dissolve
    f "Все, рабочий день закончился."
    "Отец сказал это с улыбкой, а в его голосе чувствовалась гордость."
    "Оно и понятно. Его дело перейдет мне, ведь я старший сын."
    "Мы сели в машину и поехали домой."

    scene inside_86 with dissolve
    play music citydrive
    "Меня не покидало странное чувство."
    "Ехали мы по правилам, не превышая скорости."
    "Но в голове все крутилась одна мысль…"
    "Она может {i}быстрее{/i}."
    show grandpa at left with dissolve:
        yalign -2.0
        zoom 1.2
    "Дед смотрел на меня всю дорогу."
    "Его взгляд был не совсем мне понятен."
    "Глаза выражали счастье, но было в них что-то ещё."
    "Было чувство, что он что-то скрывает и эта машина не такая простая, как кажется на первый взгляд."
    stop music
    
    scene house_ext with dissolve
    show grandpa at right 
    show dad
    with dissolve
    pause 1.5
    scene house_ent
    show grandpa at right 
    show dad
    with dissolve
    pause 1.5
    scene house_living
    show grandpa at right 
    show dad
    with dissolve
    scene house_living 
    show grandpa at right 
    show dad
    with hpunch
    hide dad with dissolve
    show grandpa at center with move 
    "Я все-таки решил окликнуть его и спросить по поводу его взгляда всю дорогу."
    "А он лишь пожал плечами и делал вид, что ничего не понимает."

    scene black with dissolve
    "Мысли о сегодняшнем дне не отпускали меня."
    "Я был переполнен эмоциями."
    "После целого дня капания в гараже, заправке машин я не чувствую себя уставшим."
    "Наоборот."
    "Я чувствую себя прекрасно."
    "Я давно не чувствовал себя таким живым."
    "Но лишь одна мысль не давала мне покоя."
    "Это взгляд деда в машине."
    "Что же он скрывает…"
    "Он ничего мне не рассказывал о жизни до встречи с моей бабушкой и рождением отца."
    "Бабушка умерла когда мне было 3."
    "Я думал, что он закроется в себе как и все, но нет."
    "Он лишь сильнее заботился о моем отце, моей маме и маленьким мне."
    "Оставив эти мысли, Я попытался уснуть."
    "В сон я провалился достаточно быстро."

    scene house_living with dissolve
    "Утром я встал легко и был готов к новому рабочему дню."
    "Сегодня отец остался дома, работы не было."
    "Мы с дедом поехали на заправку."


    scene inside_86 with dissolve
    play music citydrive
    show grandpa at left with dissolve:
        yalign -2.0
        zoom 1.2
    "Мы ехали как обычно, по правилам."
    "И вдруг дед сказал."
    g "Тут ментов нет, можешь давить на газ."
    "Эти слова меня шокировали, но перечить не стал."
    "Стрелка давно перевалила 180, а по ощущениям она ехала все быстрее и быстрее."
    g "А если так?"
    scene inside_86 with vpunch
    hide grandpa with dissolve
    play sound drift
    "И тут дедушка дёргает ручник."
    "От неожиданности я потерял управление и начал заходить в поворот боком."
    stop music
    "После поворота я остановился и чуть превыша голос спросил."
    "Ты совсем что-ли из ума выжил, старик?"
    show grandpa at left with dissolve:
        yalign -2.0
        zoom 1.2
    g "Я лишь хотел кое-что увидеть."
    mc "Что ты имеешь ввиду?"
    g "Поехали, нам надо на заправку. Машины сами себя не заправят."

    scene gasstation with dissolve:
    "Приехав на заправку я сразу приступил к работе."
    "Несмотря на большую удаленность от города, народу было много."
    "За весь рабочий день я присел только пообедать."
    scene gasstation_night with Dissolve(2.0)
    "Вечером людей стало на порядок меньше."
    "И вот конец рабочего дня."
    "Раньше я думал, что работа на заправке простая."
    "И как же я ошибался."
    scene black with dissolve
    "Голова гудела от запаха бензина и напряжённого дня."
    "Я был слишком уставшим, чтобы думать."
    "Дорога домой была спокойной и без сюрпризов."
    "Не став ужинать я сразу завалился спать."
    "Усталость дала о себе знать."
    "Вырубило меня почти моментально."
    pause 1.0

    scene gasstation with dissolve
    "Следующий день прошел намного легче, чем предыдущий."
    "Я знал что и как надо делать, где что лежит."
    "Нашел свой подход к клиентам, которые частенько оставляли мне хорошие чаевые."
    "Я и не знал, что наша заправка и мастерская настолько популярна."
    "Ничего интересного за этот день не произошло."
    "Отец был дома, помогал маме по дому."

    scene inside_86 with dissolve
    show grandpa at left with dissolve:
        yalign -2.0
        zoom 1.2
    g "Внучок, а поехали через горы. Хочу тебе кое-что показать."
    "Я возражать не стал."
    scene black with dissolve
    "К моменту как мы приехали на место уже успело стемнеть."
    scene mountain with dissolve
    "Оттуда открывался просто волшебный вид."
    show grandpa with dissolve
    g "Когда Я был в твоём возрасте, мы с друзьями частенько тут были."
    "Сзади нас пронеслись несколько машин, но видно их не было."
    mc "Это что сейчас было?"
    g "Тренировка."
    mc "Тренировка?"
    g "Да. Самые первые дрифтеры учились входить в повороты именно здесь."
    g "Здесь и зародился дрифт."
    g "Ладно, поехали домой."
    "Мы сели в машину и поехали домой"

    scene black with dissolve
    "После увиденного сегодня я не мог уснуть."
    "Сначала дед дёргает ручки, потом показывает место, где тренируются дрифтеры."
    "Что же у тебя на уме, старик?"

    scene inside_86 with dissolve
    "Я решил снова поехать на ту гору и попробовать подрифтить."
    "Благо я заправил полный бак."

    scene mountain with dissolve
    "Первые попытки были совсем плохие."
    "Несколько раз я видел как другие заходят в повороты, старался все запомнить."
    "Но все было бестолку."
    show grandpa at center with dissolve:
        zoom 0.5
        yalign 1.0
    "В какой-то момент я вижу человека, стоящего прямо посередине дороги."
    "Это был дедушка."
    show grandpa at center with dissolve:
        zoom 1.0
        yalign 1.0
    g "Так и думал, что увижу тебя здесь."
    mc "А ты чего тут забыл?"
    g "На тебя пришел посмотреть."
    "Я посмотрел на него вопросительно."
    g "Думаю пришло время тебе рассказать."
    mc "Что рассказать?"
    g "Кем Я был до встречи с твоей бабушкой и рождения твоего отца."
    "Я был просто в шоке."
    "Мой дед бывший {b}король дрифта{/b}."
    "А {b}ХАЧИРОКУ{/b} была его {b}королевой{/b}."
    mc "Я даже не знаю, что сказать."
    g "Ты ведь хочешь научиться дрифтить." 
    
    menu:
        g "Я могу научить тебя всему, чему сам научился много лет назад."
        "Принять уроки деда и учиться с ним.":
            talker "Вы официально прошли первую более-менее рабочую версию игры."
            talker "Недурно."
        "Отказаться и учиться самому.":
            talker "Вы официально прошли первую более-менее рабочую версию игры."
            talker "Недурно."
            talker "Но отказываться от услуг деда не стоило."
            talker "Он же расстроится :("

    return
