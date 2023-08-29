import json

from aiohttp.test_utils import TestCase

from tap_titans.models.player_export import PlayerExport


class ModelTest(TestCase):
    def test_player_export(self):
        PlayerExport(**json.loads(_player_export))


_player_export = '''{
    "playerStats": {
        "Max Prestige Stage": "132047",
        "Artifacts Collected": "103",
        "Crafting Power": "21",
        "Total Pet Levels": "11692",
        "Skill Points Owned": "3851",
        "Hero Weapon Upgrades": "2563",
        "Hero Scroll Upgrades": "3233",
        "Tournaments Joined": "271",
        "Undisputed Wins": "45",
        "Tournament Points": "35824",
        "Lifetime Relics": "7.974E+202"
    },
    "raidStats": {
        "Raid Level": "678",
        "Raid Damage": "778",
        "Total Raid Experience": "650738",
        "Total Raid Attacks": "4125",
        "Total Raid Card Levels": "917",
        "Raid Cards Owned": "37",
        "Wildcards": "428",
        "Lifetime Clan Morale": "31013",
        "Solo Raid World Reached": "37"
    },
    "artifacts": {
        "Book of Shadows": {
            "enchanted": "True",
            "level": "5.000E+57"
        },
        "Charged Card": {
            "enchanted": "True",
            "level": "1.000E+72"
        },
        "Stone of the Valrunes": {
            "enchanted": "True",
            "level": "1.000E+72"
        },
        "Chest of Contentment": {
            "enchanted": "True",
            "level": "1.000E+72"
        },
        "Heroic Shield": {
            "enchanted": "True",
            "level": "1.000E+72"
        },
        "Book of Prophecy": {
            "enchanted": "True",
            "level": "1.000E+63"
        },
        "Khrysos Bowl": {
            "enchanted": "False",
            "level": "1.000E+72"
        },
        "Zakynthos Coin": {
            "enchanted": "False",
            "level": "1.000E+72"
        },
        "Great Fay Medallion": {
            "enchanted": "True",
            "level": "1.200E+72"
        },
        "Neko Sculpture": {
            "enchanted": "True",
            "level": "1.000E+61"
        },
        "Coins of Ebizu": {
            "enchanted": "True",
            "level": "1.000E+72"
        },
        "The Bronzed Compass": {
            "enchanted": "True",
            "level": "1.000E+72"
        },
        "Evergrowing Stack": {
            "enchanted": "True",
            "level": "1.000E+63"
        },
        "Flute of the Soloist": {
            "enchanted": "True",
            "level": "1.000E+63"
        },
        "Heavenly Sword": {
            "enchanted": "True",
            "level": "1.300E+63"
        },
        "Divine Retribution": {
            "enchanted": "True",
            "level": "1.000E+67"
        },
        "Drunken Hammer": {
            "enchanted": "True",
            "level": "6.000E+74"
        },
        "Samosek Sword": {
            "enchanted": "True",
            "level": "2.000E+67"
        },
        "The Retaliator": {
            "enchanted": "True",
            "level": "6.000E+74"
        },
        "Stryfe's Peace": {
            "enchanted": "False",
            "level": "1.000E+67"
        },
        "Hero's Blade": {
            "enchanted": "True",
            "level": "5.000E+74"
        },
        "The Sword of Storms": {
            "enchanted": "True",
            "level": "5.000E+74"
        },
        "Furies Bow": {
            "enchanted": "True",
            "level": "5.000E+74"
        },
        "Charm of the Ancient": {
            "enchanted": "True",
            "level": "5.000E+74"
        },
        "Tiny Titan Tree": {
            "enchanted": "True",
            "level": "5.000E+74"
        },
        "Helm of Hermes": {
            "enchanted": "True",
            "level": "5.000E+74"
        },
        "Fruit of Eden": {
            "enchanted": "True",
            "level": "1.000E+57"
        },
        "Influential Elixir": {
            "enchanted": "True",
            "level": "3.000E+63"
        },
        "Shimmering Oil": {
            "enchanted": "True",
            "level": "3.000E+63"
        },
        "Golden Scope": {
            "enchanted": "True",
            "level": "3.000E+63"
        },
        "O'Ryan's Charm": {
            "enchanted": "False",
            "level": "1.200E+72"
        },
        "Heart of Storms": {
            "enchanted": "False",
            "level": "1.200E+63"
        },
        "Apollo Orb": {
            "enchanted": "False",
            "level": "1.100E+63"
        },
        "Sticky Fruit": {
            "enchanted": "False",
            "level": "1.100E+63"
        },
        "Hades Orb": {
            "enchanted": "False",
            "level": "1.100E+63"
        },
        "Earrings of Portara": {
            "enchanted": "True",
            "level": "5.000E+74"
        },
        "Avian Feather": {
            "enchanted": "True",
            "level": "5.000E+74"
        },
        "Restored Rune Heart": {
            "enchanted": "False",
            "level": "5.000E+74"
        },
        "Durendal Sword": {
            "enchanted": "True",
            "level": "1.000E+67"
        },
        "Helheim Skull": {
            "enchanted": "True",
            "level": "1.000E+67"
        },
        "Oath's Burden": {
            "enchanted": "True",
            "level": "1.100E+63"
        },
        "Crown of the Constellation": {
            "enchanted": "True",
            "level": "1.000E+63"
        },
        "Titania's Sceptre": {
            "enchanted": "True",
            "level": "1.000E+63"
        },
        "Fagin's Grip": {
            "enchanted": "True",
            "level": "1.000E+63"
        },
        "Ring of Calisto": {
            "enchanted": "True",
            "level": "1.000E+63"
        },
        "Blade of Damocles": {
            "enchanted": "True",
            "level": "1.000E+67"
        },
        "Helmet of Madness": {
            "enchanted": "True",
            "level": "1.000E+67"
        },
        "Titanium Plating": {
            "enchanted": "True",
            "level": "1.000E+67"
        },
        "Moonlight Bracelet": {
            "enchanted": "True",
            "level": "1.000E+67"
        },
        "Amethyst Staff": {
            "enchanted": "True",
            "level": "1.000E+67"
        },
        "Sword of the Royals": {
            "enchanted": "True",
            "level": "1.000E+63"
        },
        "Spearit's Vigil": {
            "enchanted": "True",
            "level": "9.000E+62"
        },
        "The Cobalt Plate": {
            "enchanted": "True",
            "level": "9.000E+62"
        },
        "Sigils of Judgement": {
            "enchanted": "True",
            "level": "9.000E+62"
        },
        "Foliage of the Keeper": {
            "enchanted": "True",
            "level": "9.000E+62"
        },
        "Invader's Gjallarhorn": {
            "enchanted": "True",
            "level": "9.000E+71"
        },
        "Titan's Mask": {
            "enchanted": "True",
            "level": "3.000E+63"
        },
        "Royal Toxin": {
            "enchanted": "True",
            "level": "4.000E+74"
        },
        "Laborer's Pendant": {
            "enchanted": "True",
            "level": "4.000E+74"
        },
        "Bringer of Ragnarok": {
            "enchanted": "True",
            "level": "4.000E+74"
        },
        "Parchment of Foresight": {
            "enchanted": "True",
            "level": "4.000E+74"
        },
        "Elixir of Eden": {
            "enchanted": "True",
            "level": "3.000E+74"
        },
        "Twin Bracers": {
            "enchanted": "True",
            "level": "3.000E+63"
        },
        "Cosmic Sextant": {
            "enchanted": "True",
            "level": "2.000E+63"
        },
        "Endless Bandolier": {
            "enchanted": "True",
            "level": "2.000E+63"
        },
        "Pearl of Oblivion": {
            "enchanted": "False",
            "level": "1.100E+67"
        },
        "Hourglass of the Impatient": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Phantom Timepiece": {
            "enchanted": "False",
            "level": "3.000E+1"
        },
        "Forbidden Scroll": {
            "enchanted": "False",
            "level": "3.000E+1"
        },
        "Ring of Fealty": {
            "enchanted": "False",
            "level": "3.000E+1"
        },
        "Glacial Axe": {
            "enchanted": "False",
            "level": "3.000E+1"
        },
        "Aegis": {
            "enchanted": "False",
            "level": "3.000E+1"
        },
        "Swamp Gauntlet": {
            "enchanted": "False",
            "level": "3.000E+1"
        },
        "Infinity Pendulum": {
            "enchanted": "False",
            "level": "2.000E+1"
        },
        "Glove of Kuma": {
            "enchanted": "False",
            "level": "3.000E+1"
        },
        "Titan Spear": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Oak Staff": {
            "enchanted": "False",
            "level": "3.000E+1"
        },
        "The Arcana Cloak": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Hunter's Ointment": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Ambrosia Elixir": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Mystic Staff": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Mystical Beans of Senzu": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Egg of Fortune": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Divine Chalice": {
            "enchanted": "False",
            "level": "5.000E+1"
        },
        "Invader's Shield": {
            "enchanted": "False",
            "level": "5.000E+1"
        },
        "Axe of Muerte": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Essence of the Kitsune": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Boots of Hermes": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Unbound Gauntlet": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Oberon Pendant": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Lucky Foot of Al-mi'raj": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Lost King's Mask": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Staff of Radiance": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Morgelai Sword": {
            "enchanted": "False",
            "level": "5.000E+1"
        },
        "Ringing Stone": {
            "enchanted": "False",
            "level": "5.000E+1"
        },
        "Quill of Scrolls": {
            "enchanted": "False",
            "level": "5.000E+1"
        },
        "Old King's Stamp": {
            "enchanted": "False",
            "level": "5.000E+1"
        },
        "The Master's Sword": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "The Magnifier": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "The Treasure of Fergus": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "The White Dwarf": {
            "enchanted": "False",
            "level": "5.000E+1"
        },
        "Aram Spear": {
            "enchanted": "False",
            "level": "4.000E+1"
        },
        "Ward of the Darkness": {
            "enchanted": "False",
            "level": "6.000E+1"
        }
    },
    "splashStats": {
        "Titan Skip": "1.1",
        "Pet Titan Skip": "0",
        "Heavenly Strike Titan Skip": "0",
        "Shadow Clone Titan Skip": "38",
        "Clanship Titan Skip": "0",
        "Dagger Titan Skip": "0",
        "Gold Gun Titan Skip": "0",
        "Stage Skip": "12",
        "Pet Stage Skip": "0",
        "Pet Skill Stage Skip": "0",
        "Dual Pet Stage Skip": "0",
        "Heavenly Strike Stage Skip": "1",
        "Shadow Clone Stage Skip": "1.15",
        "Clanship Stage Skip": "0",
        "Dagger Stage Skip": "0",
        "Dagger Target Stage Skip": "0",
        "Blade Stream Target Stage Skip": "0",
        "Magnum Opus Stage Skip": "0",
        "Golden Missile Stage Skip": "0",
        "Twilight Fairy Stage Skip": "25"
    },
    "raidCards": {
        "Moon Beam": {
            "level": 22,
            "cards": 112
        },
        "Fragmentize": {
            "level": 22,
            "cards": 0
        },
        "Skull Bash": {
            "level": 21,
            "cards": 232
        },
        "Razor Wind": {
            "level": 25,
            "cards": 52
        },
        "Whip of Lightning": {
            "level": 23,
            "cards": 16
        },
        "Clanship Barrage": {
            "level": 24,
            "cards": 90
        },
        "Purifying Blast": {
            "level": 42,
            "cards": 89
        },
        "Psychic Shackles": {
            "level": 21,
            "cards": 288
        },
        "Flak Shot": {
            "level": 24,
            "cards": 39
        },
        "Cosmic Haymaker": {
            "level": 25,
            "cards": 1
        },
        "Chain of Vengeance": {
            "level": 24,
            "cards": 154
        },
        "Mirror Force": {
            "level": 36,
            "cards": 50
        },
        "Celestial Static": {
            "level": 16,
            "cards": 763
        },
        "Blazing Inferno": {
            "level": 22,
            "cards": 283
        },
        "Acid Drench": {
            "level": 16,
            "cards": 595
        },
        "Decaying Strike": {
            "level": 21,
            "cards": 361
        },
        "Fusion Bomb": {
            "level": 20,
            "cards": 917
        },
        "Grim Shadow": {
            "level": 23,
            "cards": 1
        },
        "Thriving Plague": {
            "level": 26,
            "cards": 1
        },
        "Radioactivity": {
            "level": 25,
            "cards": 30
        },
        "Ravenous Swarm": {
            "level": 23,
            "cards": 102
        },
        "Ruinous Rain": {
            "level": 29,
            "cards": 2
        },
        "Corrosive Bubbles": {
            "level": 22,
            "cards": 7
        },
        "Maelstrom": {
            "level": 25,
            "cards": 1
        },
        "Crushing Instinct": {
            "level": 23,
            "cards": 106
        },
        "Insanity Void": {
            "level": 24,
            "cards": 113
        },
        "Rancid Gas": {
            "level": 25,
            "cards": 41
        },
        "Inspiring Force": {
            "level": 24,
            "cards": 33
        },
        "Soul Fire": {
            "level": 23,
            "cards": 57
        },
        "Victory March": {
            "level": 23,
            "cards": 6
        },
        "Prismatic Rift": {
            "level": 25,
            "cards": 144
        },
        "Ancestral Favor": {
            "level": 28,
            "cards": 5
        },
        "Grasping Vines": {
            "level": 23,
            "cards": 142
        },
        "Totem of Power": {
            "level": 42,
            "cards": 1
        },
        "Team Tactics": {
            "level": 29,
            "cards": 11
        },
        "Skeletal Smash": {
            "level": 29,
            "cards": 59
        },
        "Astral Echo": {
            "level": 22,
            "cards": 136
        }
    },
    "equipmentSets": [
        "Woodland Warrior",
        "Ruthless Necromancer",
        "Angelic Guardian",
        "Treasure Hunter",
        "Dark Predator",
        "Chaotic Alchemist",
        "Fatal Samurai",
        "Ancient Warrior",
        "Phantom Presence",
        "Cybernetic Enhancements",
        "Dragon Slayer",
        "Defender of the Egg",
        "The Heartbreaker",
        "Snow Master",
        "Midnight Raven",
        "The Rockstar",
        "Surf Strike",
        "Viking King",
        "The Sly Wolf",
        "Chained Clockwork",
        "Solar Paragon",
        "Frost Warden",
        "Toxic Slayer",
        "Defiant Spellslinger",
        "Titan Attacker",
        "Scarecrow Jack",
        "Sled Season",
        "Shadow Disciple",
        "Anniversary Platinum",
        "Mechanized Sword",
        "Chills and Thrills",
        "Lunar Festival",
        "Eternal Monk",
        "Thundering Deity",
        "Blessed Bishop",
        "Noble Fencer",
        "The Fallen Angel",
        "Dedicated Fan",
        "Bone Mender",
        "Celestial Enchanter",
        "Combo Breaker",
        "Grim Reaper",
        "Jack Frost",
        "Nimble Hunter",
        "Sweets and Treats",
        "Hidden Viper",
        "Heir of Shadows",
        "Heir of Light",
        "Kor, the Whispering Wave",
        "Styxsis, the Single Touch",
        "Digital Idol",
        "Azure Knight",
        "Grill Master",
        "Ancient Vampire",
        "Black Knight",
        "Anniversary Jade",
        "Tiny Titan",
        "Immaculate Arbiter",
        "Love Struck",
        "Brave Minstrel",
        "Forsaken Battlemage",
        "Inspiring Captain",
        "Cutthroat Razorfist",
        "Rock Queen",
        "Twilight Templar",
        "Skybound Shepherd",
        "Aquatic Defender",
        "Shae, the Radiant Beacon",
        "Fairy King",
        "Cackling Witch",
        "Spell Master",
        "Festive Bandit",
        "Inspired Lieutenant",
        "Giga-Golem",
        "Cherubic Emissary",
        "Space Knight",
        "Hell Cook",
        "Cat Ninja",
        "Forest Sylph",
        "Titan Crusher",
        "Roll Player",
        "Dungeon Explorer",
        "Cosmic Wanderer",
        "Weekend Warrior",
        "Belial, the Fossilized Symbiote",
        "Summer Sweetheart",
        "Skywing Skirmisher",
        "Headless Horsemaster",
        "Bone Knight",
        "Prestigious Champion",
        "Mad Scientist",
        "Gingerbread Master",
        "Lucky Fox Saint",
        "Tavern Dancer",
        "Scuba Diver"
    ],
    "passiveSkills": {
        "Intimidating Presence": 160,
        "Power Surge": 166,
        "Anti-Titan Cannon": 199,
        "Mystical Impact": 198,
        "Arcane Bargain": 197,
        "Silent March": 295,
        "Cloak And Dagger": 147,
        "Golden Forge": 309
    },
    "petLevels": {
        "Nova": 625,
        "Toto": 542,
        "Cerberus": 481,
        "Mousy": 511,
        "Harker": 511,
        "Bubbles": 521,
        "Demos": 520,
        "Tempest": 553,
        "Basky": 457,
        "Scraps": 509,
        "Zero": 467,
        "Polly": 478,
        "Hamy": 494,
        "Phobos": 522,
        "Fluffers": 665,
        "Kit": 536,
        "Soot": 215,
        "Klack": 238,
        "Cooper": 237,
        "Jaws": 250,
        "Xander": 259,
        "Griff": 247,
        "Basil": 242,
        "Bash": 266,
        "Violet": 239,
        "Annabelle": 229,
        "Effie": 207,
        "Percy": 231,
        "Cosmos": 212,
        "Taffy": 228
    },
    "monuments": {
        "Skull Island": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Buried Booty": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Keelhaul Reef": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Beast Hunter's Grave": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Droid Factory": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Rosabella's Village": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Freebooter Outpost": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Red Water Wreckage": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Old Salt Trading Post": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Chesterson Island": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Skyrent Valley": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Bridge of Eternal Balance": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Blessed Plains": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Void Temple": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Celestial's Thumb": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Sword Master's Shrine": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Palace of One Thousand Waterfalls": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Evergold City": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Temple of the Eternal Flame": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Freemana's Hot Springs": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "King Cobra Statue": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Twin Viper Rivers": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Nightcrag Market": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Valley of Blades": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Mound of Brothers' Meet": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Portal of Shadows": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Ancient Origin of the Vipers": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Thieves' Guild": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Hideout of Stratagem": {
            "enchanted": "False",
            "level": "0.000E+0"
        },
        "Midnight Pass": {
            "enchanted": "False",
            "level": "0.000E+0"
        }
    },
    "skillTree": {
        "Knight's Valor": 2,
        "Chivalric Order": 7,
        "Angelic Radiance": 0,
        "Will of Midas": 1,
        "Cleaving Strike": 14,
        "Rejuvenation": 0,
        "Fairy Charm": 10,
        "Barbaric Fury": 6,
        "Divine Wrath": 0,
        "Twilight Gathering": 13,
        "Eventide Afterglow": 11,
        "Pet Evolution": 2,
        "Summon Inferno": 2,
        "Heart of Gold": 0,
        "Companion Warfare": 20,
        "Ember Arts": 1,
        "Lightning Burst": 0,
        "Combat Techniques": 9,
        "Volcanic Eruption": 1,
        "Flash Zip": 0,
        "Summoning Circle": 0,
        "Burning Passion": 0,
        "Master Commander": 2,
        "Tactical Insight": 18,
        "Heroic Might": 2,
        "Aerial Assault": 0,
        "Coordinated Offensive": 0,
        "Searing Light": 4,
        "Anchoring Shot": 0,
        "Astral Awakening": 0,
        "Command Supremacy": 1,
        "Voltaic Sails": 0,
        "Galvanized Mast": 0,
        "Phantom Vengeance": 16,
        "Limit Break": 13,
        "Eternal Darkness": 15,
        "Mana Siphon": 10,
        "Manni Mana": 0,
        "Dimensional Shift": 15,
        "Lightning Strike": 1,
        "Forbidden Contract": 0,
        "Phantom Control": 11,
        "Nightmare Puppeteer": 15,
        "Terrifying Pact": 0,
        "Master Thief": 7,
        "Assassinate": 5,
        "Summon Dagger": 0,
        "Cloaking": 10,
        "Backstab": 16,
        "Poison Edge": 0,
        "Ambush": 9,
        "Deadly Focus": 6,
        "Weakpoint Throw": 0,
        "Loaded Dice": 15,
        "Mark of Death": 0,
        "Transmutation": 7,
        "Gold Gun": 0,
        "Chesterson Incense": 9,
        "Midas Ultimate": 9,
        "Magnum Opus": 0,
        "Love Potion": 10,
        "Midas Overflow": 1,
        "Auric Shot": 0,
        "Sprouting Salts": 13,
        "Royal Contract": 0,
        "Explosives Expert": 0
    }
}'''
