import random


def main() -> None:
    test_list = [120, 68, -20, 0, 5, 67, 14, 99]

    # build in immutable sort
    sorted_list = sorted(test_list)
    print(f"Original list: {test_list}")
    print(f"Sorted list: {sorted_list}")

    # built in mutable sort
    test_list.sort()
    print(f"Original list: {test_list}")

    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    shuffle_cards = random.sample(cards, k=len(cards))
    print(f"Shuffled cards: {shuffle_cards}")
    print(f"Original cards: {cards}")

    random.shuffle(cards)
    print(f"Original cards: {cards}")


if __name__ == "__main__":
    main()
