from aiohttp.test_utils import TestCase

from tap_titans.models import models


class ModelTest(TestCase):
    def test_raid_attack(self):
        models.RaidAttack(**_raid_attack)

    def test_raid_start(self):
        models.RaidStart(**_raid_start)

    def test_raid_end(self):
        models.RaidEnd(**_raid_end)

    def test_raid_retire(self):
        models.RaidRetire(**_raid_retire)

    def test_raid_cycle_reset(self):
        models.RaidCycleReset(**_raid_cycle_reset)

    def test_raid_target(self):
        models.RaidCycleReset(**_raid_cycle_reset)


_raid_attack = {
    "clan_code": "string",
    "player": {
        "name": "string",
        "code": "string",
        "raid_level": 0,
        "attack_remaining": 0
    },
    "attack_log": {
        "cards_damage": [
            {
                "titan_index": 0,
                "card_id": "MoonBeam",
                "damage_log": [
                    {
                        "id": "ArmorLegUpperRight",
                        "value": 0
                    }
                ]
            }
        ],
        "cards_level": [
            {
                "id": "MoonBeam",
                "value": 0
            }
        ],
        "attack_datetime": "2019-08-24T14:15:22Z"
    },
    "raid_state": {
        "titan_index": 0,
        "current": {
            "current_hp": 0,
            "enemy_id": "Enemy1",
            "parts": [
                {
                    "part_id": "ArmorLegUpperRight",
                    "current_hp": 0
                },
                {
                    "part_id": "ArmorLegUpperRight",
                    "current_hp": 0
                },
                {
                    "part_id": "ArmorLegUpperRight",
                    "current_hp": 0
                },
                {
                    "part_id": "ArmorLegUpperRight",
                    "current_hp": 0
                },
                {
                    "part_id": "ArmorLegUpperRight",
                    "current_hp": 0
                },
                {
                    "part_id": "ArmorLegUpperRight",
                    "current_hp": 0
                },
                {
                    "part_id": "ArmorLegUpperRight",
                    "current_hp": 0
                },
                {
                    "part_id": "ArmorLegUpperRight",
                    "current_hp": 0
                },
            ]
        }
    }
}

_raid_start = {
    "clan_code": "string",
    "player": {
        "name": "string",
        "code": "string"
    },
    "keys_remaining": 2,
    "morale": {
        "bonus": 0,
        "used": 0
    },
    "raid": {
        "level": "string",
        "tier": "string",
        "spawn_sequence": [
            "Lojak"
        ],
        "titans": [
            {
                "enemy_name": "Lojak",
                "enemy_id": "Enemy1",
                "parts": [
                    {
                        "part_id": "ArmorLegUpperRight",
                        "total_hp": 0
                    },
                    {
                        "part_id": "ArmorLegUpperRight",
                        "total_hp": 0
                    },
                    {
                        "part_id": "ArmorLegUpperRight",
                        "total_hp": 0
                    },
                    {
                        "part_id": "ArmorLegUpperRight",
                        "total_hp": 0
                    },
                    {
                        "part_id": "ArmorLegUpperRight",
                        "total_hp": 0
                    },
                    {
                        "part_id": "ArmorLegUpperRight",
                        "total_hp": 0
                    },
                    {
                        "part_id": "ArmorLegUpperRight",
                        "total_hp": 0
                    },
                    {
                        "part_id": "ArmorLegUpperRight",
                        "total_hp": 0
                    },
                ]
            }
        ]
    },
    "start_at": "2019-08-24T14:15:22Z"
}

_raid_end = {
    "clan_code": "string",
    "ended_at": "2019-08-24T14:15:22Z",
    "keys_remaining": 2,
    "raid_summary": [
        {
            "code": "string",
            "log": [
                {
                    "enemy_id": "Enemy1",
                    "titan_index": 0,
                    "damage_log": [
                        {
                            "id": "ArmorLegUpperRight",
                            "value": 0
                        }
                    ]
                }
            ]
        }
    ]
}

_raid_retire = {
    "clan_code": "string",
    "retired_at": "2019-08-24T14:15:22Z",
    "player": {
        "name": "string",
        "code": "string"
    },
    "keys_remaining": 2,
    "raid_summary": [
        {
            "code": "string",
            "log": [
                {
                    "enemy_id": "Enemy1",
                    "titan_index": 0,
                    "damage_log": [
                        {
                            "id": "ArmorLegUpperRight",
                            "value": 0
                        }
                    ]
                }
            ]
        }
    ]
}

_raid_cycle_reset = {
    "clan_code": "string",
    "next_reset_at": "2019-08-24T14:15:22Z",
    "card_bonuses": [
        {
            "id": "TeamTacticsClanMoraleBoost",
            "value": 0
        }
    ]
}

_raid_target = {
    "player": {
        "name": "string",
        "code": "string"
    },
    "titan_target": [
        {
            "enemy_id": "Enemy1",
            "state": "22001100"
        }
    ]
}
