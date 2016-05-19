# -*- coding: utf-8 -*-
eshop = {"mleko": 0.99, "sir": 3.46, "banana": 0.67, "jogurt": 0.82, "sok": 1.45, "solata": 1.34, "plenice": 12.99, "sampon": 2.19, "milo": 0.45}

def main(izdelek):
    if izdelek in eshop.keys():
        return eshop[izdelek]
    else:
        return False


if __name__ == "__main__":
    izdelek = raw_input("Izberi izdelek, če želiš ugotoviti ceno: ").lower()
    cena = main(izdelek)


