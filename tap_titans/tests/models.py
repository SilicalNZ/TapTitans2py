from aiohttp.test_utils import TestCase

from tap_titans.models import models


class ModelTest(TestCase):
    def test_raid_unsub_clan(self):
        models.ClanRemoved(**_clan_unsub)

    def test_raid_attack(self):
        models.RaidAttack(**_raid_attack)

    def test_raid_start(self):
        models.RaidStart(**_raid_start)

    def test_raid_sub_start(self):
        models.RaidStart(**_raid_sub_start)

    def test_raid_end(self):
        models.RaidEnd(**_raid_end)

    def test_raid_retire(self):
        models.RaidRetire(**_raid_retire)

    def test_raid_cycle_reset(self):
        models.RaidCycleReset(**_raid_cycle_reset)

    def test_raid_sub_cycle(self):
        models.RaidCycleReset(**_sub_cycle)

    def test_raid_target(self):
        models.RaidCycleReset(**_raid_cycle_reset)


_clan_unsub = {
    "clan_code": "string",
    "namespace": "string"
}

_raid_attack = {
    "clan_code": "string",
    "raid_id": 0,
    "player": {
        "name": "string",
        "player_code": "string",
        "raid_level": 0,
        "attack_remaining": 0
    },
    "attack_log": {
        "cards_damage": [
            {
                "titan_index": 0,
                "id": "MoonBeam",
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
    "raid_id": 0,
    "player": {
        "name": "string",
        "player_code": "string"
    },
    "keys_remaining": 2,
    "morale": {
        "bonus": {
            "BonusType": "string",
            "BonusAmount": 0
        },
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
                "total_hp": 0,
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

_raid_sub_start = {
    "clan_code": "string",
    "raid_id": 0,
    "player": {
        "name": "string",
        "player_code": "string"
    },
    "keys_remaining": 2,
    "morale": {
        "bonus": {
            "BonusType": "string",
            "BonusAmount": 0
        },
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
                "total_hp": 0,
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
    "raid_id": 0,
    "ended_at": "2019-08-24T14:15:22Z",
    "keys_remaining": 2,
    "raid_summary": [
        {
            "player_code": "string",
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
    "raid_id": 0,
    "retired_at": "2019-08-24T14:15:22Z",
    "player": {
        "name": "string",
        "player_code": "string"
    },
    "keys_remaining": 2,
    "raid_summary": [
        {
            "player_code": "string",
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
    "raid_id": 0,
    "raid": {
        "tier": 0,
        "level": 0
    },
    "next_reset_at": "2019-08-24T14:15:22Z",
    "card_bonuses": [
        {
            "id": "TeamTacticsClanMoraleBoost",
            "value": 0
        }
    ]
}

_sub_cycle = {
    "clan_code": "string",
    "raid_id": 0,
    "raid": {
        "tier": 0,
        "level": 0
    },
    "next_reset_at": "2019-08-24T14:15:22Z",
    "card_bonuses": [
        {
            "id": "TeamTacticsClanMoraleBoost",
            "value": 0
        }
    ]
}

_raid_target = {
    "raid_id": 0,
    "player": {
        "name": "string",
        "player_code": "string"
    },
    "titan_target": [
        {
            "enemy_id": "Enemy1",
            "state": [
                {
                    "id": "Head",
                    "state": 0
                }
            ]
        }
    ]
}
