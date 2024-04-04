from datetime import datetime


def get_start_msg(lang):
    if lang == "ru":
        return """
Привет, {username}!

<b>Решение NamTool — это решение с открытым исходным кодом, которое предоставляет обновленную информацию о состоянии вашего узла и ключевые сведения о сети, расширяя возможности мониторинга сети.</b>

Начните использовать инструмент NamTool с настройки мониторинга узла и проверки состояния сети. Кроме того, рассмотрите возможность настройки оповещения X, чтобы оставаться в курсе обновлений Namada. Вы также можете выбрать родной язык через настройки.

Свяжитесь с нами: https://x.com/_deNodes.

Благодарим вас за использование NamTool!"""

    elif lang == "ua":
        return """
Привіт, {username}!

<b>Рішення NamTool — це рішення з відкритим вихідним кодом, яке надає оновлення стану вашого вузла та ключову статистику мережі, покращуючи ваш досвід моніторингу мережі.</b>

Почніть використовувати інструменти NamTool, налаштувавши моніторинг вузла та перевіривши стан мережі. Крім того, подумайте про налаштування сповіщення X, щоб бути в курсі оновлень Namada. Ви також можете вибрати свою рідну мову через налаштування.

Зв’яжіться з нами: https://x.com/_deNodes.

Дякуємо за використання NamTool!"""

    else:
        return """
Hey, <code>{username}</code> !

<b>The NamTool solution is an open-source solution that provides updates on your node status and key network insights, enhancing your network monitoring experience.</b>

Start using the NamTool tool by setting up node monitoring and checking the network status. Additionally, consider setting up an alert to stay informed about status updates. You can also select your preferred language in the settings.

Reach out to us: https://x.com/_deNodes.

Thank you for using NamTool!"""


def get_explore_namada(lang):
    if lang == "ru":
        return """
<b>Что такое Намада?</b>

<a href="https://namada.net/">Namada</a> — это протокол уровня 1 Proof-of-Stake, в котором особое внимание уделяется конфиденциальности между активами между цепочками. Сеть полностью поддерживает протокол IBC, включает в себя собственный мост Ethereum и предлагает современную систему доказательства доли с автоматическим начислением вознаграждения и кубическим дроблением.

Пользователи, участвующие в защищенных передачах, получают в качестве вознаграждения токены собственного протокола, что повышает конфиденциальность.
Кроме того, Namada предлагает кошелек для защищенных переводов с несколькими активами, обеспечивающий безопасное и конфиденциальное взаимодействие пользователя с протоколом.

<b>Вот несколько сообщений в блоге, которые помогут вам лучше понять протокол:</b>
- <a href="https://namada.net/blog/introducing-namada-interchain-asset-agnostic-privacy">Представляем конфиденциальность мультичейна, независимую от активов</a>
- <a href="https://namada.net/blog/what-is-namada">Что такое сеть Намада?</a>
- <a href="https://namada.net/blog/shaping-multichain-privacy">Формирование конфиденциальности мультичейна</a>
- <a href="https://namada.net/blog/understanding-the-masp-and-cc-circuits">Как работает экранированный пул с несколькими активами</a>
- <a href="https://namada.net/blog/the-namada-ethereum-bridge">Мост Намада Эфириум</a>

<b>Официальные ресурсы:</b>
<a href="https://namada.net/">Веб-сайт</a> // <a href="https://twitter.com/namada">X (Twitter)</a> // <a href="https://discord.com/invite/namada">Discord</a>
<a href="https://github.com/anoma/namada">Github</a> // <a href="https://docs.namada.net/">Документация</a> // <a href="https://t.me/namadaprotocol">Telegram</a>
"""
    elif lang == "ua":
        return """
<b>Що таке Намада?</b>

<a href="https://namada.net/">Namada</a> — це протокол рівня 1 Proof-of-Stake, який наголошує на конфіденційності міжланцюгових активів. Мережа повністю підтримує протокол IBC, включає власний міст Ethereum і пропонує сучасну систему підтвердження частки з автоматичним складанням винагороди та кубічним скороченням.

Користувачі, які беруть участь у захищених передачах, отримують токени рідного протоколу як винагороду, що підвищує конфіденційність.
Крім того, Namada пропонує екранований гаманець для передачі кількох активів для забезпечення безпечної та приватної взаємодії користувача з протоколом.

<b>Ось кілька публікацій у блозі, які допоможуть вам краще зрозуміти протокол:</b>
- <a href="https://namada.net/blog/introducing-namada-interchain-asset-agnostic-privacy">Представлення агностичної конфіденційності багатоланцюжків активів</a>
- <a href="https://namada.net/blog/what-is-namada">Що таке мережа Namada?</a>
- <a href="https://namada.net/blog/shaping-multichain-privacy">Формування конфіденційності Multichain</a>
- <a href="https://namada.net/blog/understanding-the-masp-and-cc-circuits">Як працює екранований пул із багатьма активами</a>
- <a href="https://namada.net/blog/the-namada-ethereum-bridge">The Namada Ethereum Bridge</a>

<b>Офіційні ресурси:</b>
<a href="https://namada.net/">Веб-сайт</a> // <a href="https://twitter.com/namada">X (Twitter)</a> // <a href="https://discord.com/invite/namada">Discord</a>
<a href="https://github.com/anoma/namada">Github</a> // <a href="https://docs.namada.net/">Документи</a> // <a href="https://t.me/namadaprotocol">Telegram</a>
"""
    else:
        return """
<b>What is Namada?</b>

<a href="https://namada.net/">Namada</a> is a Proof-of-Stake Layer 1 protocol that emphasizes interchain asset-agnostic privacy. The network fully supports the IBC protocol, includes a native Ethereum bridge, and offers a modern proof-of-stake system with automatic reward compounding and cubic slashing.

Users participating in shielded transfers receive native protocol tokens as rewards, enhancing privacy.
Moreover, Namada offers a multi-asset shielded transfer wallet to ensure secure and private user interaction with the protocol.

<b>Here are some blog posts to help you understand the protocol better:</b>
- <a href="https://namada.net/blog/introducing-namada-interchain-asset-agnostic-privacy">Introducing Asset Agnostic Multichain Privacy</a>
- <a href="https://namada.net/blog/what-is-namada">What is Namada network?</a>
- <a href="https://namada.net/blog/shaping-multichain-privacy">Shaping Multichain Privacy</a>
- <a href="https://namada.net/blog/understanding-the-masp-and-cc-circuits">How does the Multi-Asset Shielded Pool works</a>
- <a href="https://namada.net/blog/the-namada-ethereum-bridge">The Namada Ethereum Bridge</a>

<b>Official Resources:</b>
<a href="https://namada.net/">Website</a> // <a href="https://twitter.com/namada">X (Twitter)</a> // <a href="https://discord.com/invite/namada">Discord</a>
<a href="https://github.com/anoma/namada">Github</a> // <a href="https://docs.namada.net/">Docs</a> // <a href="https://t.me/namadaprotocol">Telegram</a> 
"""



def get_run_node(lang):
    if lang == "ru":
        return """
<b>Запуск ноды Намада</b>

Чтобы упростить запуск узла Namada, вы можете использовать скрипт, представленный ниже, и выбрать дополнительные параметры через свой терминал:
<pre>
wget -q -O namada.sh https://api.denodes.xyz/namada.sh && chmod +x namada.sh && sudo /bin/bash namada.sh
</pre>
Подробное руководство можно найти в <a href="https://hub.denodes.xyz/namada/node-setup-guide/">Руководстве по узлу Namada</a>.
"""
    elif lang == "ua":
        return """
<b>Запуск ноди Namada</b>

Щоб спростити запуск вузла Namada, ви можете скористатися наданим нижче скриптом і вибрати додаткові параметри через свій термінал:
<pre>
wget -q -O namada.sh https://api.denodes.xyz/namada.sh && chmod +x namada.sh && sudo /bin/bash namada.sh
</pre>
Щоб отримати повний посібник, зверніться до <a href="https://hub.denodes.xyz/namada/node-setup-guide/">Посібника з вузлів Namada</a>.
"""
    else:
        return """
<b>Run a Namada Node</b>

To make running a Namada node easier, you can use the script provided below and select additional options through your terminal:
<pre>
wget -q -O namada.sh https://api.denodes.xyz/namada.sh && chmod +x namada.sh && sudo /bin/bash namada.sh
</pre>
For a comprehensive guide, refer to the <a href="https://hub.denodes.xyz/namada/node-setup-guide/">Namada Node Guide</a>.
"""


def get_contact_us(lang):
    if lang == "ru":
        return """
<b>Поддержка.</b> Если вам нужна помощь или вы хотите сообщить о проблеме, не стесняйтесь обращаться к нам через https://x.com/_denodes.
<b>Вклад</b>. Внесите свой вклад в наш проект на <a href="https://github.com/denodesxyz/namtool">GitHub</a>. Мы ценим любой вклад, включая улучшения кода, обновления документации, отчеты об ошибках, переводы и предложения новых функций.
"""
    elif lang == "ua":
        return """
<b>Підтримка:</b> якщо вам потрібна допомога або ви хочете повідомити про проблему, без вагань зв’яжіться з нами через https://x.com/_denodes.
<b>Внесок:</b> Зробіть внесок у наш проект на <a href="https://github.com/denodesxyz/namtool">GitHub</a>. Ми цінуємо внески будь-якого роду, включаючи вдосконалення коду, оновлення документів, звіти про помилки, переклади та пропозиції нових функцій.
"""
    else:
        return """
<b>Support:</b> If you need assistance or wish to report a problem, don't hesitate to contact us through https://x.com/_denodes.

<b>Contributing:</b> Contribute to our project on <a href="https://github.com/denodesxyz/namtool">GitHub</a>. We appreciate contributions of any kind, including code improvements, docs updates, bug reports, translations, and new feature suggestions.
"""


def get_language(lang):
    if lang == "ru":
        return """
Пожалуйста, выберите свой родной язык для бота NamTool из списка ниже.

Если вашего языка нет в списке, рассмотрите возможность внести свой вклад в наш <a href="https://github.com/denodesxyz/namtool">GitHub</a>, чтобы расширить возможности языка и повысить удобство использования.
"""

    elif lang == "ua":
        return """
Виберіть свою рідну мову зі списку нижче для бота NamTool.

Якщо вашої мови немає в списку, спробуйте зробити внесок у наш <a href="https://github.com/denodesxyz/namtool">GitHub</a>, щоб розширити мовні параметри та покращити зручність використання.
"""
    else:
        return """
<b>Please choose your native language from the list below for the NamTool bot.</b>

If your language is not listed, consider contributing to our <a href="https://github.com/denodesxyz/namtool">GitHub</a> to help expand the language options and enhance usability.
"""



def get_node_alert(lang):
    if lang == "ru":
        return """Хотите ли вы получать оповещение, если ваш узел выйдет из строя?"""
    elif lang == "ua":
        return """Ви хочете отримувати сповіщення, якщо ваш вузол вийде з ладу?"""
    else:
        return """Do you want to receive an alert if your node goes down?"""


def get_discord_alert(lang):
    if lang == "ru":
        return """Хотите следить за обновлениями <a href="https://discord.com/invite/namada">Namada</a> в дискорде?"""
    elif lang == "ua":
        return """Ви бажаєте стежити за оновленнями <a href="https://discord.com/invite/namada">Namada</a> в діскорді?"""
    else:
        return """Do you want to follow the <a href="https://discord.com/invite/namada">Namada</a> updates on Discord?"""


def get_state_alert(lang):
    if lang == "ru":
        return """Хотите получать обновления об изменении состояния вашей ноды?"""
    elif lang == "ua":
        return """Бажаєте отримувати оновлення про зміну стану вашої ноди?"""
    else:
        return """Do you want to receive updates about changing state of your node?"""

def get_vote_alert(lang):
    if lang == "ru":
        return """Хотите получать обновления о новых голосованиях?"""
    elif lang == "ua":
        return """Бажаєте отримувати оновлення про нові голосування?"""
    else:
        return """Do you want to receive updates about new votes?"""


def get_halt_alert(lang):
    if lang == "ru":
        return """Хотите получать обновления о новых хальтах?"""
    elif lang == "ua":
        return """Бажаєте отримувати оновлення про нові хальти?"""
    else:
        return """Do you want to receive updates about new halts?"""

def get_remove_node(lang):
    if lang == "ru":
        return """Хотите удалить свою ноду из бота?"""
    elif lang == "ua":
        return """Ви хочете видалити свій вузол із бота?"""
    else:
        return """Do you want to remove your node from the bot?"""


def get_remove_node(lang):
    if lang == "ru":
        return """Хотите удалить свою ноду из бота?"""
    elif lang == "ua":
        return """Ви хочете видалити свій вузол із бота?"""
    else:
        return """Do you want to remove your node from the bot?"""


def get_node_status_not_exist(lang):
    if lang == "ru":
        return """
<b>Статус ноды</b>

Чтобы отслеживать <b>статус вашей ноды</b>, вам необходимо сначала настроить его, а затем ввести свой <b>узел RPC</b> ниже. Следуйте <a href="https://github.com/denodesxyz/namtool">руководству</a> здесь, чтобы упростить настройку.

Кроме того, вы можете выбрать получение оповещений при изменении статуса вашего узла, изменив свои предпочтения в настройках.
"""
    elif lang == "ua":
        return """
<b>Статус ноди</b>

Щоб контролювати <b>статус вашої ноди</b>, вам потрібно спочатку налаштувати його, а потім ввести свій <b>вузол RPC</b> нижче. Дотримуйтеся <a href="https://github.com/denodesxyz/namtool">посібника</a> тут, щоб легко налаштувати.

Крім того, ви можете вибрати отримання сповіщень про зміни в статусі вашого вузла, налаштувавши свої параметри в налаштуваннях.
"""
    else:
        return """
<b>Node Status</b>

To monitor the <b>status of your node</b>, you need to set it up first and then input your <b>RPC node</b> below. Please follow the <a href="https://github.com/denodesxyz/namtool">guide</a> here for an easy setup.

Furthermore, you can opt to receive alerts if there are changes to your node's status by adjusting your preferences in the Settings.
"""
    


def get_settings_text(lang):
    if lang == "ru":
        return "Настройки"
    elif lang == "ua":
        return "Налаштування"
    else:
        return "Settings"


def get_success_text(lang):
    if lang == "ru":
        return "Успешно"
    elif lang == "ua":
        return "Успішно"
    else:
        return "Success"

def get_main_menu_text(lang):
    if lang == "ru":
        return "Главное меню"
    elif lang == "ua":
        return "Головне меню"
    else:
        return "Main menu"

def get_node_status_text(lang):
    if lang == "ru":
        return """<b>Статус вашей ноды:</b> {ip}

Moniker: <b>{moniker}</b>
Catching Up: <b>{catching}</b>
Active Set: <b>{active}</b>
Uptime: <b>{uptime}%</b>
Tendermint Address: <b>{addr}</b>
"""
    elif lang == "ua":
        return """<b>Статус вашої ноди:</b> {ip}

Moniker: <b>{moniker}</b>
Catching Up: <b>{catching}</b>
Active Set: <b>{active}</b>
Uptime: <b>{uptime}%</b>
Tendermint Address: <b>{addr}</b>
"""
    else:
        return """<b>Status of Your Node:</b> {ip}

Moniker: <b>{moniker}</b>
Catching Up: <b>{catching}</b>
Height: <b>{height}</b>
Active Set: <b>{active}</b>
Uptime: <b>{uptime}%</b>
Tendermint Address: <b>{addr}</b>
"""


def get_new_node_success_text(lang):
    if lang == "ru":
        return """Поздравляем. Ваша нода успешно зарегистрирована!"""
    elif lang == "ua":
        return """Вітаємо. Вашу ноду успішно зареєстровано!"""
    else:
        return """Congratulations. Your node has been registered successfully!"""


def get_new_node_failure_text(lang):
    if lang == "ru":
        return """Если вы не входите в активный набор валидаторов, вы можете получить статус узла, открыв rpc следующим образом"""
    elif lang == "ua":
        return """Якщо ви не в активному наборі перевірки, ви можете отримати статус вузла, відкривши rpc наступним чином"""
    else:
        return """If you're not in the active validator set, you can obtain the node status by opening an rpc as follows"""


def get_error_invalid_ipv4(lang):
    if lang == "ru":
        return "Пожалуйста введите валидный IPV4 адрес"
    elif lang == "ua":
        return "Будь ласка введіть валідний IPV4 адрес"
    else:
        return "Please enter a valid IPV4 address"


def get_network_status_text(lang):
    if lang == "ru":
        return "Статус Сети"
    elif lang == "ua":
        return "Статус мережі"
    else:
        return "Network Status"


def get_nosuchnetwork_text(lang):
    if lang == "ru":
        return "Такой сети нет. Выберите сеть из списка ниже"
    elif lang == "ua":
        return "Такої мережі немає. Виберіть мережу зі списку нижче"
    else:
        return "No such network. Choose a network from the list below"

def get_noinfonetwork_text(lang):
    if lang == "ru":
        return "На данный момент нет информации об этой сети"
    elif lang == "ua":
        return "На даний момент немає інформації про цю мережу"
    else:
        return "No info about this network at the current moment"

def get_nodeisnotcathingup_text(lang):
    if lang == "ru":
        return "⚠️ Ваша нода {ip} отстаёт! Последний блок: {block}"
    elif lang == "ua":
        return "⚠️ Ваша нода {ip} відстає! Останній блок: {block}"
    else:
        return "⚠️ Your node {ip} is cathing up! Latest block: {block}"

def get_nodeisnotavailable_text(lang):
    if lang == "ru":
        return "🚨 Ваша нода {ip} недоступна"
    elif lang == "ua":
        return "🚨 Ваша нода {ip} недоступна"
    else:
        return "🚨 Your node {ip} is unavailable!"

def get_nodatafornode_text(lang):
    if lang == "ru":
        return "🚨 Нет данных для {ip}! Пожалуйста, отправьте правильные данные"
    elif lang == "ua":
        return "🚨 Немає даних для {ip}! Будь ласка, надішліть правильні дані"
    else:
        return "🚨 No data for {ip}! Please submit the correct data"


def get_vote_text(lang, proposal):
    if lang == "ru":
        return f"""Голосование за предложение #{proposal['id']} открыто
<b>id:</b> {proposal['id']}
<b>authors:</b> {proposal['content']['authors']}
<b>author:</b> {proposal['author']}
<b>type:</b> {proposal['type']}
<b>created:</b> {proposal['content']['created']}
<b>voting_start_epoch:</b> {proposal['voting_start_epoch']}
<b>voting_end_epoch:</b> {proposal['voting_end_epoch']}
<b>title:</b>{proposal['content'].get('title', '')}
<b>abstract:</b> {proposal['content'].get('abstract', '-')}
<b>details:</b> {proposal['content'].get('details', '-')}
<b>motivation:</b> {proposal['content'].get('motivation', '-')}
<b>discussions-to:</b> {proposal['content'].get('discussions-to', '-')}
"""
    elif lang == "ua":
        return f"""Голосування за пропозицію #{proposal['id']} відкрито
<b>id:</b> {proposal['id']}
<b>authors:</b> {proposal['content']['authors']}
<b>author:</b> {proposal['author']}
<b>type:</b> {proposal['type']}
<b>created:</b> {proposal['content']['created']}
<b>voting_start_epoch:</b> {proposal['voting_start_epoch']}
<b>voting_end_epoch:</b> {proposal['voting_end_epoch']}
<b>title:</b>{proposal['content'].get('title', '')}
<b>abstract:</b> {proposal['content'].get('abstract', '-')}
<b>details:</b> {proposal['content'].get('details', '-')}
<b>motivation:</b> {proposal['content'].get('motivation', '-')}
<b>discussions-to:</b> {proposal['content'].get('discussions-to', '-')}
"""
    else:
        return f"""Voting for proposal #{proposal['id']} is now open
<b>id:</b> {proposal['id']}
<b>authors:</b> {proposal['content']['authors']}
<b>author:</b> {proposal['author']}
<b>type:</b> {proposal['type']}
<b>created:</b> {proposal['content'].get('created', '-')}
<b>voting_start_epoch:</b> {proposal['voting_start_epoch']}
<b>voting_end_epoch:</b> {proposal['voting_end_epoch']}
<b>title:</b>{proposal['content'].get('title', '')}
<b>abstract:</b> {proposal['content'].get('abstract', '-')}
<b>details:</b> {proposal['content'].get('details', '-')}
<b>motivation:</b> {proposal['content'].get('motivation', '-')}
<b>discussions-to:</b> {proposal['content'].get('discussions-to', '-')}
"""

def get_wrong_rpc_address(lang):
    if lang == "ru":
        return "Неверный адрес"
    elif lang == "ua":
        return "Невірний адрес"
    else:
        return "Wrong address"


def get_node_changed_state(lang, ip, before, after):
    if lang == "ru":
        return f"Ваша нода <b>{ip}</b> изменила свое состояние с <b>{before}</b> на <b>{after}</b>"
    elif lang == "ua":
        return f"Ваша нода <b>{ip}</b> змінила свій стан з <b>{before}</b> на <b>{after}</b>"
    else:
        return f"Your node <b>{ip}</b> has changed state from <b>{before}</b> to <b>{after}</b>"

def get_node_addr_not_state(lang, ip):
    if lang == "ru":
        return f"Ваша нода <b>{ip}</b> не находится в списке валидаторов"
    elif lang == "ua":
        return f"Ваша нода <b>{ip}</b> не знаходиться у списку валідаторів"
    else:
        return f"Your node <b>{ip}</b> is not in the validators list"


def get_address_data(lang, data, uptime):
    if lang == "ru":
        return f"""<b>Moniker:</b> {data.get('moniker', '-')}
<b>Address:</b> {data['address']}
<b>Tendermint address:</b> {data['tm-address']}
<b>Tokens bonded:</b> {data['bonded']}
<b>State:</b> {data['state']}
<b>Uptime:</b> {uptime}%"""
    elif lang == "ua":
        return f"""<b>Moniker:</b> {data.get('moniker', '-')}
<b>Address:</b> {data['address']}
<b>Tendermint address:</b> {data['tm-address']}
<b>Tokens bonded:</b> {data['bonded']}
<b>State:</b> {data['state']}
<b>Uptime:</b> {uptime}%"""
    else:
        return f"""<b>Moniker:</b> {data.get('moniker', '-')}
<b>Address:</b> {data['address']}
<b>Tendermint address:</b> {data['tm-address']}
<b>Tokens bonded:</b> {data['bonded']}
<b>State:</b> {data['state']}
<b>Uptime:</b> {uptime}%"""


def get_low_uptime(lang, value):
    if lang == "ru":
        return f"Аптайм вашей ноды опустился ниже <b>{value}%</b>"
    elif lang == "ua":
        return f"Аптайм вашої ноди опустився нижче <b>{value}%</b>"
    else:
        return f"Uptime of your node is less than <b>{value}%</b>"


def get_new_halt(lang, value):
    now = datetime.now().strftime("%H:%M:%S %Y-%m-%d")
    if lang == "ru":
        return f"🛑 Цепочка остановилась на последнем блоке № {value} в {now}."
    elif lang == "en":
        return f"🛑 Ланцюжок зупинився на останньому блоці #{value} о {now}"
    else:
        return f"🛑 The chain has halted at the latest block #{value} at {now}"
