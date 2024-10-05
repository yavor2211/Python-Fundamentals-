lost_fights=int(input())
helmet_price=float(input())
sword_price=float(input())
shield_price=float(input())
armor_price=float(input())

helmet_broken= lost_fights // 2
sword_broken= lost_fights // 3
shield_broken= lost_fights // (2 * 3)
armor_broken=shield_broken // 2

total_expenses= helmet_broken * helmet_price \
                + sword_broken * sword_price \
                + shield_broken * shield_price \
                + armor_broken * armor_price
print(f"Gladiator expenses: {total_expenses:.2f} aureus")
