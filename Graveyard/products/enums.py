from enum import Enum
import pycountry


class VPNType(str, Enum):
    WIREGUARD = "Wireguard"
    OPENVPN = "OpenVPN"
    IKEV2 = "IKEV2"
    L2TP = "L2TP"
    V2RAY = "V2Ray"
    SSH = "SSH"

    @classmethod
    def choices(cls):
        return [(member.value, member.value) for member in cls]  # Store and display the same value


class GiftcardType(str, Enum):
    PLAYSTATION = "PlayStation"
    XBOX = "Xbox"
    SPOTIFY = "Spotify"
    APPLESTORE = "Apple Store"
    GOOGLEPLAY = "Google Play"

    @classmethod
    def choices(cls):
        return [(member.value, member.value) for member in cls]  # Store and display the same value


class Country(str, Enum):
    @classmethod
    def choices(cls):
        return [(country.alpha_2, country.name) for country in pycountry.countries]

    @classmethod
    def get_name(cls, code):
        country = pycountry.countries.get(alpha_2=code)
        return country.name if country else None
