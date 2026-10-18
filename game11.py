
import random

# ================================================
# ИГРА «ЗАБРОШЕННЫЕ ШАХТЫ»
# Этап 11 — инвентарь и характеристики в словаре
# Бонус эликсира прибавляется после расчёта критического удара.
# Каждая штука эликсира добавляет +2 урона к каждому удару.
# ================================================

title = "ЗАБРОШЕННЫЕ ШАХТЫ"
frame = "=" * 31

print(frame)
print(title)
print(frame)

print("Как зовут героя?")
hero_name = input()

print(f"Добро пожаловать, {hero_name}!")
print("Ты входишь в шахту. Здесь темно и сыро.")
print()

# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")

while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        vinoslivost = int(input())

        if health <= 0:
            raise ValueError(
                f"Здоровье должно быть положительным, а введено {health}"
            )

        if strength < 0:
            raise ValueError(
                f"Сила не может быть отрицательной, а введено {strength}"
            )

        if agility < 0:
            raise ValueError(
                f"Ловкость не может быть отрицательной, а введено {agility}"
            )

        if vinoslivost < 0:
            raise ValueError(
                f"Выносливость не может быть отрицательной, а введено {vinoslivost}"
            )

        break

    except ValueError as e:
        print(f"{e}. Введите все четыре характеристики снова:")

# --- Расчёт характеристик ---------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2

max_stamina = vinoslivost * 3 + 2
stamina = max_stamina

# Максимальные значения на начало забега
max_health = health
max_stamina = stamina

print()
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Выносливость: {vinoslivost}")
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил: {stamina}")
print()

# --- Враги и их характеристики ----------------------
# Имена в enemies совпадают с ключами enemy_stats.

enemies = ["ghoul", "skeleton", "spider", "bat"]

enemy_names = {
    "ghoul": "упырь",
    "skeleton": "скелет",
    "spider": "паук",
    "bat": "летучая мышь"
}

enemy_stats = {
    "skeleton": {"hp": 45, "damage": 6, "loot": 25},
    "ghoul": {"hp": 30, "damage": 4, "loot": 15},
    "spider": {"hp": 20, "damage": 3, "loot": 10},
    "bat": {"hp": 12, "damage": 2, "loot": 5}
}

# --- Магазин ----------------------------------------
prices = {
    "potion": 10,
    "torch_oil": 15,
    "war_elixir": 40
}

# --- Рюкзак и журнал боя ----------------------------
inventory = {}
log = []

# Каждая запись журнала:
# [номер раунда, урон героя, урон врага]

# Золото и бонус урона за весь забег
gold_total = 0
ability_bonus = 0


# --- Функции игры -----------------------------------

def hero_hit(strike_n):
    """Принимает номер удара.
    Возвращает пару (урон, признак критического удара).
    Читает глобальные damage и crit_damage, ничего не изменяет.
    """
    if strike_n % 3 == 0:
        return crit_damage, True

    return damage, False


def fight(enemy, hero_health, bonus=0):
    """Бой с enemy до гибели одного из двоих.

    Карточка врага берётся из enemy_stats по имени.
    Нужны ключи hp, damage, loot.
    Бонус прибавляется после расчёта критического удара
    и сам не удваивается.
    Возвращает (rounds, won, hero_health, loot).
    Печатает раунды боя, не изменяет глобальные переменные.
    """
    stats = enemy_stats[enemy]
    enemy_hp = float(stats["hp"])
    rounds = []
    round_n = 0

    print("Ты спускаешься по лестнице в темноту.")
    print(f"Из темноты появляется {enemy_names[enemy]}!")

    while enemy_hp > 0 and hero_health > 0:
        round_n += 1

        # --- Удар героя -----------------------------
        hit, crit = hero_hit(round_n)
        hit += bonus
        enemy_hp -= hit

        if crit:
            line = (
                f"Раунд {round_n}: ты наносишь "
                f"{hit:.1f} урона — критический удар!"
            )
        else:
            line = (
                f"Раунд {round_n}: ты наносишь "
                f"{hit:.1f} урона."
            )

        # --- Враг побеждён --------------------------
        if enemy_hp <= 0:
            line += " Враг повержен."
            rounds.append([round_n, hit, 0])
            print(line)
            break

        # --- Ответный удар врага --------------------
        blow = stats["damage"]
        hero_health -= blow

        line += (
            f" Здоровье врага: {enemy_hp:.1f}. "
            f"{enemy_names[enemy].capitalize()} наносит {blow} урона."
        )

        rounds.append([round_n, hit, blow])
        print(line)

    # --- Награда за победу --------------------------
    won = enemy_hp <= 0
    loot = stats["loot"] if won else 0

    return rounds, won, hero_health, loot


def print_leaderboard(log):
    """Принимает журнал боёв.
    Возвращает None.
    Печатает топ-3 раундов по урону героя и самый сильный удар врага.
    """
    if not log:
        print("Ты ещё не участвовал в боях.")
        return

    top = sorted(
        log,
        key=lambda r: r[1],
        reverse=True
    )[:3]

    print("Таблица лидеров — урон героя:")

    for i in range(len(top)):
        print(
            f"{i + 1}. Раунд {top[i][0]}: "
            f"{top[i][1]:.1f}"
        )

    worst = max(log, key=lambda r: r[2])

    print(
        f"Самый сильный удар врага: {worst[2]} "
        f"(раунд {worst[0]})."
    )


def print_run_summary(log):
    """Принимает журнал боёв.
    Возвращает None.
    Печатает суммарный и средний урон героя за забег.
    """
    total = sum(r[1] for r in log)
    rounds = len(log)

    if rounds > 0:
        print(
            f"Урон: {total:.1f} за {rounds} раундов, "
            f"в среднем {total / rounds:.1f}."
        )
    else:
        print("В этом забеге боёв не было.")


def buy(price, gold, quantity=1):
    """Принимает цену, имеющееся золото и количество quantity=1.
    Возвращает (gold_left, ok): остаток золота и успех покупки.
    Ничего не печатает и не изменяет глобальные переменные.
    """
    cost = price * quantity

    if quantity <= 0 or gold < cost:
        return gold, False

    return gold - cost, True


# --- Подготовка игры --------------------------------
running = True
actions = 0
menu_last = 11
outcome = "прерывание"


# --- Главный цикл -----------------------------------
try:
    while running:
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - прислушаться")
        print("5 - зажечь факел")
        print("6 - тренировка")
        print("7 - спуститься глубже")
        print("8 - таблица лидеров")
        print("9 - магазин")
        print("10 - рюкзак")
        print("11 - выпить зелье")
        print("0 - выйти из шахт")
        print()

        # --- Проверка ввода меню --------------------
        while True:
            choice = input()

            try:
                menu_number = int(choice)
            except ValueError:
                print("Введи целый номер одного из пунктов меню.")
                continue

            if 0 <= menu_number <= menu_last:
                break

            print(f"Такого пункта нет. Введи номер от 0 до {menu_last}.")

        # --- Выбор действия --------------------------
        match str(menu_number):
            case "0":
                print("Ты поднимаешься к выходу. Шахты остаются позади.")
                outcome = "выход"
                running = False

            case "1":
                print("Ты осмотрелся. Вокруг старые вагонетки и обломки камней.")

            case "2":
                cost = 2

                if stamina >= cost:
                    stamina -= cost
                    print("Ты осторожно идёшь вперёд. Под ногами хрустит камень.")
                else:
                    health -= cost - stamina
                    stamina = 0
                    print("Сил больше нет — приходится идти на одном упорстве.")
                    print("Недостаток сил отнимает здоровье!")

            case "3":
                recovery = 3
                stamina = min(stamina + recovery, max_stamina)
                print("Ты немного отдыхаешь и восстанавливаешь силы.")

            case "4":
                print("Ты прислушался. Из глубины шахты доносится странный звук.")

            case "5":
                if stamina >= 1:
                    stamina -= 1
                    print("Ты зажёг факел. Стало немного светлее.")
                else:
                    print("У тебя недостаточно сил, чтобы зажечь факел.")

            case "6":
                strikes = 6
                total_damage = 0
                crit_count = 0

                print("Ты подходишь к старому тренировочному чучелу.")
                print(f"Наносишь {strikes} ударов:")

                for i in range(1, strikes + 1):
                    hit_damage, crit = hero_hit(i)

                    if crit:
                        crit_count += 1
                        print(f"Удар {i}: {hit_damage:.1f} — критический!")
                    else:
                        print(f"Удар {i}: {hit_damage:.1f}")

                    total_damage += hit_damage

                training_cost = 3

                if stamina >= training_cost:
                    stamina -= training_cost
                else:
                    health -= training_cost - stamina
                    stamina = 0
                    print("На тренировку не хватило сил. Ты истощён!")

                print()
                print(f"Всего ударов: {strikes}")
                print(f"Критических ударов: {crit_count}")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")

            case "7":
                if not enemies:
                    print("Ты спускаешься глубже, но подземелье уже пусто.")
                else:
                    enemy = random.choice(enemies)

                    rounds, won, health, loot = fight(
                        enemy,
                        health,
                        bonus=ability_bonus
                    )

                    # Журнал пополняется вне функции боя
                    for r in rounds:
                        log.append(r)

                    if won:
                        gold_total += loot
                        enemies.remove(enemy)

                        print(
                            f"{enemy_names[enemy].capitalize()} побеждён! "
                            f"В шахтах осталось врагов: {len(enemies)}. "
                            f"Добыча: {loot} золота."
                        )

                    print(f"Бой длился {len(rounds)} раундов.")

            case "8":
                print_leaderboard(log)

            case "9":
                print("Магазин:")

                for name, price in prices.items():
                    print(f"{name}: {price} золота")

                print("Название предмета (пустая строка — отмена покупки):")
                name = input().strip()

                if name != "":
                    if name in prices:
                        price = prices[name]

                        print("Количество (Enter — одна штука):")
                        qty_line = input().strip()

                        try:
                            if qty_line == "":
                                qty = 1
                                gold_total, ok = buy(price, gold_total)
                            else:
                                qty = int(qty_line)

                                if qty <= 0:
                                    print("Количество должно быть больше нуля.")
                                    ok = False
                                else:
                                    gold_total, ok = buy(
                                        price,
                                        gold_total,
                                        quantity=qty
                                    )

                            if qty > 0 and ok:
                                # Добавляем купленные предметы в рюкзак
                                inventory[name] = inventory.get(name, 0) + qty

                                # Сохраняем прежние эффекты этапа 10.
                                # Зелье теперь восстанавливает здоровье
                                # только при использовании в пункте 11.
                                if name == "torch_oil":
                                    stamina = min(
                                        stamina + 5 * qty,
                                        max_stamina
                                    )

                                elif name == "war_elixir":
                                    ability_bonus += 2 * qty

                                print(
                                    f"Куплено: {qty} шт. {name} "
                                    f"за {price * qty} золота. "
                                    f"Осталось золота: {gold_total}."
                                )

                            elif qty > 0:
                                print(
                                    f"Недостаточно золота: нужно "
                                    f"{price * qty}, у тебя {gold_total}."
                                )

                        except ValueError:
                            print("Введи целое число или нажми Enter.")

                    else:
                        print("Такого предмета в магазине нет.")

            case "10":
                if not inventory:
                    print("Рюкзак пуст.")
                else:
                    print("Рюкзак:")

                    for name, qty in inventory.items():
                        print(f"{name}: {qty} шт.")

            case "11":
                if inventory.get("potion", 0) == 0:
                    print("В рюкзаке нет зелий.")
                else:
                    health = min(health + 10, max_health)
                    inventory["potion"] -= 1

                    if inventory["potion"] == 0:
                        del inventory["potion"]

                    print(
                        f"Ты выпиваешь зелье. Здоровье: {health}. "
                        f"Зелий осталось: {inventory.get('potion', 0)}."
                    )

        # --- Счётчик действий ------------------------
        if menu_number != 0:
            actions += 1

        # --- Состояние героя --------------------------
        print()
        print(
            f"Здоровье: {health} | "
            f"Запас сил: {stamina} | "
            f"Осталось врагов: {len(enemies)} | "
            f"Золото: {gold_total}"
        )

        # --- Проверка гибели --------------------------
        if health <= 0:
            print()
            print("Ты падаешь без сил. Шахты забирают ещё одного искателя.")
            outcome = "гибель"
            running = False

        print()

except KeyboardInterrupt:
    print()
    print("Ты прервал исследование шахт.")

finally:
    print(frame)

    if inventory:
        print("В рюкзаке осталось:")

        for name, qty in inventory.items():
            print(f"{name}: {qty} шт.")
    else:
        print("В рюкзаке ничего не осталось.")

    if outcome == "гибель":
        print(f"Ты не дошёл до конца, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Ты выбрался из шахт, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Исследование прервано, {hero_name}. Действий совершено: {actions}.")

    print_run_summary(log)

    print(frame)
