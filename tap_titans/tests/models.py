from unittest import TestCase

from tap_titans.models import models


class ModelTest(TestCase):
    def test_raid_unsub_clan(self):
        models.clan_models.ClanRemoved.decode_json(_clan_unsub)

    def test_raid_attack(self):
        models.raid_models.RaidAttackEnd.decode_json(_raid_attack_end)

    def test_raid_start(self):
        models.raid_models.RaidStart.decode_json(_raid_start)

    def test_raid_start_clan_added(self):
        models.raid_models.RaidStartClanAdded.decode_json(_raid_start_clan_added)

    def test_raid_end(self):
        models.raid_models.RaidEnd.decode_json(_raid_end)

    def test_raid_retire(self):
        models.raid_models.RaidRetire.decode_json(_raid_retire)

    def test_raid_cycle_reset(self):
        models.raid_models.RaidCycleReset.decode_json(_raid_cycle_reset)

    def test_raid_sub_cycle(self):
        models.raid_models.RaidCycleResetClanAdded.decode_json(_sub_cycle)

    def test_raid_target(self):
        models.raid_models.RaidTarget.decode_json(_raid_target)

    def test_player_morale(self):
        models.clan_models.PlayerMorale.decode_json(_player_morale)

    def test_raid_attack_started(self):
        models.raid_models.RaidAttackStart.decode_json(_raid_attack_start)

    def test_clan_kick(self):
        models.clan_models.ClanKick.decode_json(_clan_kick)

    def test_clan_leave(self):
        models.clan_models.ClanLeave.decode_json(_clan_leave)

    def test_clan_join(self):
        models.clan_models.ClanJoin.decode_json(_clan_join)

    def test_clan_sync(self):
        models.clan_models.ClanSync.decode_json(_clan_sync)

    def test_player_data(self):
        models.player_models.PlayerData.decode_json(_player_data)


_raid_start = '''{"clan_code": "test", "keys_remaining": 1,
               "morale": {"bonus_amount": 0.25, "used": 0},
               "player": {"name": "test", "player_code": "test"},
               "raid": {"area_buffs": [{"bonus_amount": 3.0, "bonus_type": "RaidAttackDuration"}], "level": "1",
                        "spawn_sequence": ["Jukk", "Sterl", "Takedar"], "tier": "9999", "titans": [
                       {"area_debuffs": [{"bonus_amount": 0.5, "bonus_type": "AllLimbsHPMult"}], "enemy_id": "Enemy2",
                        "enemy_name": "Takedar", "parts": [{"part_id": "BodyHead", "total_hp": 1468800000.0},
                                                           {"part_id": "ArmorHead", "total_hp": 1224000000.0},
                                                           {"part_id": "BodyChestUpper", "total_hp": 1224000000.0},
                                                           {"part_id": "ArmorChestUpper", "total_hp": 1020000000.0},
                                                           {"part_id": "BodyArmUpperRight", "total_hp": 382500000.0},
                                                           {"part_id": "ArmorArmUpperRight", "total_hp": 306000000.0},
                                                           {"part_id": "BodyArmUpperLeft", "total_hp": 382500000.0},
                                                           {"part_id": "ArmorArmUpperLeft", "total_hp": 306000000.0},
                                                           {"part_id": "BodyLegUpperRight", "total_hp": 459000000.0},
                                                           {"part_id": "ArmorLegUpperRight", "total_hp": 459000000.0},
                                                           {"part_id": "BodyLegUpperLeft", "total_hp": 459000000.0},
                                                           {"part_id": "ArmorLegUpperLeft", "total_hp": 459000000.0},
                                                           {"part_id": "BodyHandRight", "total_hp": 382500000.0},
                                                           {"part_id": "ArmorHandRight", "total_hp": 306000000.0},
                                                           {"part_id": "BodyHandLeft", "total_hp": 382500000.0},
                                                           {"part_id": "ArmorHandLeft", "total_hp": 306000000.0}],
                        "total_hp": 4080000000.0},
                       {"area_debuffs": [{"bonus_amount": 0.5, "bonus_type": "ArmorArmsHPMult"}], "enemy_id": "Enemy3",
                        "enemy_name": "Jukk", "parts": [{"part_id": "BodyHead", "total_hp": 1428000000.0},
                                                        {"part_id": "ArmorHead", "total_hp": 1020000000.0},
                                                        {"part_id": "BodyChestUpper", "total_hp": 1428000000.0},
                                                        {"part_id": "ArmorChestUpper", "total_hp": 1020000000.0},
                                                        {"part_id": "BodyArmUpperRight", "total_hp": 357000000.0},
                                                        {"part_id": "ArmorArmUpperRight", "total_hp": 382500000.0},
                                                        {"part_id": "BodyArmUpperLeft", "total_hp": 357000000.0},
                                                        {"part_id": "ArmorArmUpperLeft", "total_hp": 382500000.0},
                                                        {"part_id": "BodyLegUpperRight", "total_hp": 714000000.0},
                                                        {"part_id": "ArmorLegUpperRight", "total_hp": 510000000.0},
                                                        {"part_id": "BodyLegUpperLeft", "total_hp": 714000000.0},
                                                        {"part_id": "ArmorLegUpperLeft", "total_hp": 510000000.0},
                                                        {"part_id": "BodyHandRight", "total_hp": 357000000.0},
                                                        {"part_id": "ArmorHandRight", "total_hp": 382500000.0},
                                                        {"part_id": "BodyHandLeft", "total_hp": 357000000.0},
                                                        {"part_id": "ArmorHandLeft", "total_hp": 382500000.0}],
                        "total_hp": 4080000000.0},
                       {"area_debuffs": [{"bonus_amount": 0.45, "bonus_type": "ArmorLegsHPMult"}], "enemy_id": "Enemy4",
                        "enemy_name": "Sterl", "parts": [{"part_id": "BodyHead", "total_hp": 816000000.0},
                                                         {"part_id": "ArmorHead", "total_hp": 816000000.0},
                                                         {"part_id": "BodyChestUpper", "total_hp": 2692800000.0},
                                                         {"part_id": "ArmorChestUpper", "total_hp": 1020000000.0},
                                                         {"part_id": "BodyArmUpperRight", "total_hp": 204000000.0},
                                                         {"part_id": "ArmorArmUpperRight", "total_hp": 255000000.0},
                                                         {"part_id": "BodyArmUpperLeft", "total_hp": 204000000.0},
                                                         {"part_id": "ArmorArmUpperLeft", "total_hp": 255000000.0},
                                                         {"part_id": "BodyLegUpperRight", "total_hp": 408000000.0},
                                                         {"part_id": "ArmorLegUpperRight", "total_hp": 739500000.0},
                                                         {"part_id": "BodyLegUpperLeft", "total_hp": 408000000.0},
                                                         {"part_id": "ArmorLegUpperLeft", "total_hp": 739500000.0},
                                                         {"part_id": "BodyHandRight", "total_hp": 204000000.0},
                                                         {"part_id": "ArmorHandRight", "total_hp": 255000000.0},
                                                         {"part_id": "BodyHandLeft", "total_hp": 204000000.0},
                                                         {"part_id": "ArmorHandLeft", "total_hp": 255000000.0}],
                        "total_hp": 4080000000.0}]}, "raid_id": 2889500, "start_at": "2023-08-20T12:00:31Z"}'''

_raid_start_clan_added = '''{"clan_code": "test", "raid_id": 2991065, "keys_remaining": 1,
                          "morale": {"bonus_amount": 0.45, "used": 30000},
                          "raid": {"spawn_sequence": ["Jukk", "Sterl", "Jukk", "Mohaca", "Mohaca", "Mohaca"],
                                   "tier": 9999, "level": 63, "titans": [
                                  {"enemy_id": "Enemy3", "total_hp": 4800000000.0,
                                   "parts": [{"part_id": "BodyHead", "total_hp": 1680000000.0, "cursed": false},
                                             {"part_id": "ArmorHead", "total_hp": 1200000000.0, "cursed": false},
                                             {"part_id": "BodyChestUpper", "total_hp": 1680000000.0, "cursed": false},
                                             {"part_id": "ArmorChestUpper", "total_hp": 1200000000.0, "cursed": true},
                                             {"part_id": "BodyArmUpperRight", "total_hp": 210000000.0, "cursed": false},
                                             {"part_id": "ArmorArmUpperRight", "total_hp": 150000000.0, "cursed": true},
                                             {"part_id": "BodyArmUpperLeft", "total_hp": 210000000.0, "cursed": false},
                                             {"part_id": "ArmorArmUpperLeft", "total_hp": 150000000.0, "cursed": true},
                                             {"part_id": "BodyLegUpperRight", "total_hp": 420000000.0, "cursed": false},
                                             {"part_id": "ArmorLegUpperRight", "total_hp": 300000000.0,
                                              "cursed": false},
                                             {"part_id": "BodyLegUpperLeft", "total_hp": 420000000.0, "cursed": false},
                                             {"part_id": "ArmorLegUpperLeft", "total_hp": 300000000.0, "cursed": true},
                                             {"part_id": "BodyHandRight", "total_hp": 210000000.0, "cursed": false},
                                             {"part_id": "ArmorHandRight", "total_hp": 150000000.0, "cursed": false},
                                             {"part_id": "BodyHandLeft", "total_hp": 210000000.0, "cursed": false},
                                             {"part_id": "ArmorHandLeft", "total_hp": 150000000.0, "cursed": false}],
                                   "enemy_name": "Jukk",
                                   "area_debuffs": [{"bonus_type": "AllLimbsHPMult", "bonus_amount": -0.5}],
                                   "cursed_debuffs": [{"bonus_type": "BodyDamagePerCurse", "bonus_amount": -0.06}]},
                                  {"enemy_id": "Enemy4", "total_hp": 4800000000.0,
                                   "parts": [{"part_id": "BodyHead", "total_hp": 960000000.0, "cursed": false},
                                             {"part_id": "ArmorHead", "total_hp": 960000000.0, "cursed": false},
                                             {"part_id": "BodyChestUpper", "total_hp": 3168000000.0, "cursed": false},
                                             {"part_id": "ArmorChestUpper", "total_hp": 1200000000.0, "cursed": false},
                                             {"part_id": "BodyArmUpperRight", "total_hp": 360000000.0, "cursed": false},
                                             {"part_id": "ArmorArmUpperRight", "total_hp": 450000000.0, "cursed": true},
                                             {"part_id": "BodyArmUpperLeft", "total_hp": 360000000.0, "cursed": false},
                                             {"part_id": "ArmorArmUpperLeft", "total_hp": 450000000.0, "cursed": false},
                                             {"part_id": "BodyLegUpperRight", "total_hp": 720000000.0, "cursed": false},
                                             {"part_id": "ArmorLegUpperRight", "total_hp": 900000000.0, "cursed": true},
                                             {"part_id": "BodyLegUpperLeft", "total_hp": 720000000.0, "cursed": false},
                                             {"part_id": "ArmorLegUpperLeft", "total_hp": 900000000.0, "cursed": true},
                                             {"part_id": "BodyHandRight", "total_hp": 360000000.0, "cursed": false},
                                             {"part_id": "ArmorHandRight", "total_hp": 450000000.0, "cursed": true},
                                             {"part_id": "BodyHandLeft", "total_hp": 360000000.0, "cursed": false},
                                             {"part_id": "ArmorHandLeft", "total_hp": 450000000.0, "cursed": false}],
                                   "enemy_name": "Sterl",
                                   "area_debuffs": [{"bonus_type": "AllLimbsHPMult", "bonus_amount": 0.5}],
                                   "cursed_debuffs": [
                                       {"bonus_type": "AfflictedDamagePerCurse", "bonus_amount": -0.06}]},
                                  {"enemy_id": "Enemy5", "total_hp": 4800000000.0,
                                   "parts": [{"part_id": "BodyHead", "total_hp": 1200000000.0, "cursed": false},
                                             {"part_id": "ArmorHead", "total_hp": 1200000000.0, "cursed": true},
                                             {"part_id": "BodyChestUpper", "total_hp": 1200000000.0, "cursed": false},
                                             {"part_id": "ArmorChestUpper", "total_hp": 2400000000.0, "cursed": false},
                                             {"part_id": "BodyArmUpperRight", "total_hp": 720000000.0, "cursed": false},
                                             {"part_id": "ArmorArmUpperRight", "total_hp": 450000000.0, "cursed": true},
                                             {"part_id": "BodyArmUpperLeft", "total_hp": 720000000.0, "cursed": false},
                                             {"part_id": "ArmorArmUpperLeft", "total_hp": 450000000.0, "cursed": false},
                                             {"part_id": "BodyLegUpperRight", "total_hp": 984000000.0, "cursed": false},
                                             {"part_id": "ArmorLegUpperRight", "total_hp": 600000000.0,
                                              "cursed": false},
                                             {"part_id": "BodyLegUpperLeft", "total_hp": 984000000.0, "cursed": false},
                                             {"part_id": "ArmorLegUpperLeft", "total_hp": 600000000.0, "cursed": false},
                                             {"part_id": "BodyHandRight", "total_hp": 720000000.0, "cursed": false},
                                             {"part_id": "ArmorHandRight", "total_hp": 450000000.0, "cursed": true},
                                             {"part_id": "BodyHandLeft", "total_hp": 720000000.0, "cursed": false},
                                             {"part_id": "ArmorHandLeft", "total_hp": 450000000.0, "cursed": true}],
                                   "enemy_name": "Mohaca",
                                   "area_debuffs": [{"bonus_type": "AllArmsHPMult", "bonus_amount": 0.5}],
                                   "cursed_debuffs": [
                                       {"bonus_type": "AfflictedDamagePerCurse", "bonus_amount": -0.06}]}],
                                   "area_buffs": [{"bonus_type": "HeadDamage", "bonus_amount": 0.3}]},
                          "start_at": "2024-03-04T00:03:34Z", "titan_target": [{"enemy_id": "Enemy3",
                                                                                "state": [{"id": "Head", "state": "0"},
                                                                                          {"id": "ChestUpper",
                                                                                           "state": "0"},
                                                                                          {"id": "ArmUpperRight",
                                                                                           "state": "0"},
                                                                                          {"id": "ArmUpperLeft",
                                                                                           "state": "0"},
                                                                                          {"id": "LegUpperRight",
                                                                                           "state": "0"},
                                                                                          {"id": "LegUpperLeft",
                                                                                           "state": "0"},
                                                                                          {"id": "HandRight",
                                                                                           "state": "0"},
                                                                                          {"id": "HandLeft",
                                                                                           "state": "0"}]},
                                                                               {"enemy_id": "Enemy4",
                                                                                "state": [{"id": "Head", "state": "0"},
                                                                                          {"id": "ChestUpper",
                                                                                           "state": "0"},
                                                                                          {"id": "ArmUpperRight",
                                                                                           "state": "0"},
                                                                                          {"id": "ArmUpperLeft",
                                                                                           "state": "0"},
                                                                                          {"id": "LegUpperRight",
                                                                                           "state": "0"},
                                                                                          {"id": "LegUpperLeft",
                                                                                           "state": "0"},
                                                                                          {"id": "HandRight",
                                                                                           "state": "0"},
                                                                                          {"id": "HandLeft",
                                                                                           "state": "0"}]},
                                                                               {"enemy_id": "Enemy5",
                                                                                "state": [{"id": "Head", "state": "0"},
                                                                                          {"id": "ChestUpper",
                                                                                           "state": "0"},
                                                                                          {"id": "ArmUpperRight",
                                                                                           "state": "0"},
                                                                                          {"id": "ArmUpperLeft",
                                                                                           "state": "0"},
                                                                                          {"id": "LegUpperRight",
                                                                                           "state": "0"},
                                                                                          {"id": "LegUpperLeft",
                                                                                           "state": "0"},
                                                                                          {"id": "HandRight",
                                                                                           "state": "0"},
                                                                                          {"id": "HandLeft",
                                                                                           "state": "0"}]}]}'''

_clan_unsub = '''{
    "clan_code": "string",
    "namespace": "string",
    "token": "b5507016-7da2-4777-a161-1e8042a6a377"
}'''

_raid_attack_end = '''{"attack_log": {"attack_datetime": "2023-06-25T12:04:20Z", "cards_damage": [
    {"titan_index": 0, "id": null, "damage_log": [{"id": "ArmorLegUpperRight", "value": 9165775}]},
    {"titan_index": 0, "id": "LimbSupport", "damage_log": []},
    {"titan_index": 0, "id": "Haymaker", "damage_log": [{"id": "ArmorLegUpperRight", "value": 24201592}]}],
                               "cards_level": [{"id": "LimbSupport", "value": 25}, {"id": "Haymaker", "value": 29},
                                               {"id": "AstralEcho", "value": 44}]}, "clan_code": "test",
                "raid_id": 123,
                "cycle": 3,
                "player": {"attacks_remaining": 5, "player_code": "test", "name": "test", "raid_level": 700},
                "raid_state": {"current": {"enemy_id": "Enemy7", "current_hp": 3662999993.0,
                                           "parts": [{"part_id": "BodyHead", "current_hp": 1505900000.0},
                                                     {"part_id": "ArmorHead", "current_hp": 1177297855.0},
                                                     {"part_id": "BodyChestUpper", "current_hp": 1872200000.0},
                                                     {"part_id": "ArmorChestUpper", "current_hp": 1211329190.0},
                                                     {"part_id": "BodyArmUpperRight", "current_hp": 549450000.0},
                                                     {"part_id": "ArmorArmUpperRight", "current_hp": 826088850.0},
                                                     {"part_id": "BodyArmUpperLeft", "current_hp": 549450000.0},
                                                     {"part_id": "ArmorArmUpperLeft", "current_hp": 826492148.0},
                                                     {"part_id": "BodyLegUpperRight", "current_hp": 183150000.0},
                                                     {"part_id": "ArmorLegUpperRight", "current_hp": 369419222.0},
                                                     {"part_id": "BodyLegUpperLeft", "current_hp": 183150000.0},
                                                     {"part_id": "ArmorLegUpperLeft", "current_hp": 403146919.0},
                                                     {"part_id": "BodyHandRight", "current_hp": 549450000.0},
                                                     {"part_id": "ArmorHandRight", "current_hp": 832376472.0},
                                                     {"part_id": "BodyHandLeft", "current_hp": 549450000.0},
                                                     {"part_id": "ArmorHandLeft", "current_hp": 835579661.0}]},
                               "titan_index": 0}}'''

_raid_end = '''{
    "clan_code": "string",
    "raid_id": 0,
    "ended_at": "2019-08-24T14:15:22Z",
    "keys_remaining": 2,
    "raid_summary": [
        {
            "player_code": "string",
            "name": "string",
            "num_attacks": 0,
            "total_damage": 0,
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
}'''

_raid_retire = '''{
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
            "name": "string",
            "num_attacks": 0,
            "total_damage": 0,
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
}'''

_raid_cycle_reset = '''{
    "clan_code": "string",
    "raid_id": 0,
    "morale": {"bonus_amount": 0.341, "used": 13695},
    "started_at": "2019-08-24T14:15:22Z",
    "raid_started_at": "2019-08-24T14:15:22Z",
    "next_reset_at": "2019-08-24T14:15:22Z",
    "card_bonuses": [
        {
            "id": "TeamTacticsClanMoraleBoost",
            "value": 0.452299999999999946
        }
    ]
}'''

_sub_cycle = '''{"card_bonuses": [{"id": "MirrorForceBoost", "value": 0.35},
                               {"id": "TeamTacticsClanMoraleBoost", "value": 0.062299999999999946}],
              "clan_code": "test", "next_reset_at": "2023-07-15T00:00:22Z",
              "morale": {"bonus_amount": 0.341, "used": 13695},
              "raid": {"area_buffs": [{"bonus_amount": 0.15, "bonus_type": "AllRaidDamage"}], "level": "68",
                       "spawn_sequence": ["Terro", "Mohaca", "Sterl", "Terro", "Terro", "Sterl", "Mohaca", "Terro"],
                       "tier": "9999", "titans": [
                      {"area_debuffs": [{"bonus_amount": 0.5, "bonus_type": "AllLimbsHPMult"}],
                       "cursed_debuffs": [{"bonus_amount": -0.06, "bonus_type": "BodyDamagePerCurse"}],
                       "enemy_id": "Enemy4", "enemy_name": "Sterl",
                       "parts": [{"cursed": false, "part_id": "BodyHead", "total_hp": 816000000.0},
                                 {"cursed": true, "part_id": "ArmorHead", "total_hp": 816000000.0},
                                 {"cursed": false, "part_id": "BodyChestUpper", "total_hp": 2692800000.0},
                                 {"cursed": false, "part_id": "ArmorChestUpper", "total_hp": 1020000000.0},
                                 {"cursed": false, "part_id": "BodyArmUpperRight", "total_hp": 306000000.0},
                                 {"cursed": false, "part_id": "ArmorArmUpperRight", "total_hp": 382500000.0},
                                 {"cursed": false, "part_id": "BodyArmUpperLeft", "total_hp": 306000000.0},
                                 {"cursed": true, "part_id": "ArmorArmUpperLeft", "total_hp": 382500000.0},
                                 {"cursed": false, "part_id": "BodyLegUpperRight", "total_hp": 612000000.0},
                                 {"cursed": true, "part_id": "ArmorLegUpperRight", "total_hp": 765000000.0},
                                 {"cursed": false, "part_id": "BodyLegUpperLeft", "total_hp": 612000000.0},
                                 {"cursed": false, "part_id": "ArmorLegUpperLeft", "total_hp": 765000000.0},
                                 {"cursed": false, "part_id": "BodyHandRight", "total_hp": 306000000.0},
                                 {"cursed": true, "part_id": "ArmorHandRight", "total_hp": 382500000.0},
                                 {"cursed": false, "part_id": "BodyHandLeft", "total_hp": 306000000.0},
                                 {"cursed": false, "part_id": "ArmorHandLeft", "total_hp": 382500000.0}],
                       "total_hp": 4080000000.0},
                      {"area_debuffs": [{"bonus_amount": 0.5, "bonus_type": "AllArmsHPMult"}],
                       "cursed_debuffs": [{"bonus_amount": -0.06, "bonus_type": "AfflictedDamagePerCurse"}],
                       "enemy_id": "Enemy5", "enemy_name": "Mohaca",
                       "parts": [{"cursed": false, "part_id": "BodyHead", "total_hp": 1020000000.0},
                                 {"cursed": false, "part_id": "ArmorHead", "total_hp": 1020000000.0},
                                 {"cursed": false, "part_id": "BodyChestUpper", "total_hp": 1020000000.0},
                                 {"cursed": false, "part_id": "ArmorChestUpper", "total_hp": 2040000000.0},
                                 {"cursed": false, "part_id": "BodyArmUpperRight", "total_hp": 612000000.0},
                                 {"cursed": false, "part_id": "ArmorArmUpperRight", "total_hp": 382500000.0},
                                 {"cursed": false, "part_id": "BodyArmUpperLeft", "total_hp": 612000000.0},
                                 {"cursed": false, "part_id": "ArmorArmUpperLeft", "total_hp": 382500000.0},
                                 {"cursed": false, "part_id": "BodyLegUpperRight", "total_hp": 836400000.0},
                                 {"cursed": true, "part_id": "ArmorLegUpperRight", "total_hp": 510000000.0},
                                 {"cursed": false, "part_id": "BodyLegUpperLeft", "total_hp": 836400000.0},
                                 {"cursed": true, "part_id": "ArmorLegUpperLeft", "total_hp": 510000000.0},
                                 {"cursed": false, "part_id": "BodyHandRight", "total_hp": 612000000.0},
                                 {"cursed": true, "part_id": "ArmorHandRight", "total_hp": 382500000.0},
                                 {"cursed": false, "part_id": "BodyHandLeft", "total_hp": 612000000.0},
                                 {"cursed": true, "part_id": "ArmorHandLeft", "total_hp": 382500000.0}],
                       "total_hp": 4080000000.0},
                      {"area_debuffs": [{"bonus_amount": 0.5, "bonus_type": "ArmorLegsHPMult"}],
                       "cursed_debuffs": [{"bonus_amount": -0.06, "bonus_type": "AfflictedDamagePerCurse"}],
                       "enemy_id": "Enemy6", "enemy_name": "Terro",
                       "parts": [{"cursed": false, "part_id": "BodyHead", "total_hp": 1101600000.0},
                                 {"cursed": true, "part_id": "ArmorHead", "total_hp": 1142400000.0},
                                 {"cursed": false, "part_id": "BodyChestUpper", "total_hp": 1550400000.0},
                                 {"cursed": false, "part_id": "ArmorChestUpper", "total_hp": 1999200000.0},
                                 {"cursed": false, "part_id": "BodyArmUpperRight", "total_hp": 224400000.0},
                                 {"cursed": true, "part_id": "ArmorArmUpperRight", "total_hp": 255000000.0},
                                 {"cursed": false, "part_id": "BodyArmUpperLeft", "total_hp": 224400000.0},
                                 {"cursed": false, "part_id": "ArmorArmUpperLeft", "total_hp": 255000000.0},
                                 {"cursed": false, "part_id": "BodyLegUpperRight", "total_hp": 448800000.0},
                                 {"cursed": true, "part_id": "ArmorLegUpperRight", "total_hp": 642600000.0},
                                 {"cursed": false, "part_id": "BodyLegUpperLeft", "total_hp": 448800000.0},
                                 {"cursed": false, "part_id": "ArmorLegUpperLeft", "total_hp": 642600000.0},
                                 {"cursed": false, "part_id": "BodyHandRight", "total_hp": 224400000.0},
                                 {"cursed": false, "part_id": "ArmorHandRight", "total_hp": 255000000.0},
                                 {"cursed": false, "part_id": "BodyHandLeft", "total_hp": 224400000.0},
                                 {"cursed": true, "part_id": "ArmorHandLeft", "total_hp": 255000000.0}],
                       "total_hp": 3060000000.0}]}, "raid_id": 2865891, "raid_started_at": "2023-07-13T00:00:22Z",
              "titan_target": [{"enemy_id": "Enemy4",
                                "state": [{"id": "Head", "state": "2"}, {"id": "ChestUpper", "state": "2"},
                                          {"id": "ArmUpperRight", "state": "2"}, {"id": "ArmUpperLeft", "state": "2"},
                                          {"id": "LegUpperRight", "state": "1"}, {"id": "LegUpperLeft", "state": "1"},
                                          {"id": "HandRight", "state": "2"}, {"id": "HandLeft", "state": "2"}]},
                               {"enemy_id": "Enemy5",
                                "state": [{"id": "Head", "state": "1"}, {"id": "ChestUpper", "state": "1"},
                                          {"id": "ArmUpperRight", "state": "2"}, {"id": "ArmUpperLeft", "state": "2"},
                                          {"id": "LegUpperRight", "state": "2"}, {"id": "LegUpperLeft", "state": "2"},
                                          {"id": "HandRight", "state": "2"}, {"id": "HandLeft", "state": "2"}]},
                               {"enemy_id": "Enemy6",
                                "state": [{"id": "Head", "state": "1"}, {"id": "ChestUpper", "state": "2"},
                                          {"id": "ArmUpperRight", "state": "2"}, {"id": "ArmUpperLeft", "state": "2"},
                                          {"id": "LegUpperRight", "state": "2"}, {"id": "LegUpperLeft", "state": "2"},
                                          {"id": "HandRight", "state": "2"}, {"id": "HandLeft", "state": "2"}]}]}'''

_raid_target = '''{"clan_code": "test", "enemy_id": "Enemy2", "player": {"name": "test", "player_code": "test"},
        "raid_id": 2894808, "state": [{"id": "Head", "state": "2"}, {"id": "ChestUpper", "state": "2"},
                                      {"id": "ArmUpperRight", "state": "2"}, {"id": "ArmUpperLeft", "state": "2"},
                                      {"id": "LegUpperRight", "state": "1"}, {"id": "LegUpperLeft", "state": "1"},
                                      {"id": "HandRight", "state": "2"}, {"id": "HandLeft", "state": "2"}],
        "updated_at": "2023-08-29T05:12:11Z"}'''

_player_morale = '''{"amount": 11, "clan_code": "test", "player": {"name": "test", "player_code": "test"}}'''

_raid_attack_start = '''{"cards": ["PowerBubble", "MentalFocus", "DecayingAttack"], "clan_code": "test", "player": {"name": "test", "player_code": "test"}, "raid_id": 2983816, "started_at": "2024-02-19T15:01:26Z"}'''

_clan_kick = '''{"clan_code": "test", "executor": {"name": "test", "player_code": "test"}, "player": {"name": "test", "player_code": "test"}}'''

_clan_leave = '''{"clan_code": "test", "player": {"name": "test", "player_code": "test"}}'''

_clan_join = '''{"clan_code": "test", "player": {"name": "test", "player_code": "test"}}'''

_clan_sync = '''{"clan_code": "test", "clan_name": "test"}'''

_player_data = '''{"additive_relic_multiplier": 80196, "artifacts": [{"artifact_id": "Artifact1", "is_enchanted": true, "level": "1.71511011000000E+102"}, {"artifact_id": "Artifact10", "is_enchanted": true, "level": "1.82033244400000E+106"}, {"artifact_id": "Artifact100", "is_enchanted": true, "level": "1.02377699900000E+106"}, {"artifact_id": "Artifact101", "is_enchanted": true, "level": "7.05175269000000E+92"}, {"artifact_id": "Artifact102", "is_enchanted": true, "level": "7.05175269000000E+92"}, {"artifact_id": "Artifact103", "is_enchanted": true, "level": "3.39263583600000E+95"}, {"artifact_id": "Artifact11", "is_enchanted": true, "level": "7.46607210800000E+92"}, {"artifact_id": "Artifact12", "is_enchanted": false, "level": "30"}, {"artifact_id": "Artifact13", "is_enchanted": false, "level": "30"}, {"artifact_id": "Artifact14", "is_enchanted": false, "level": "30"}, {"artifact_id": "Artifact15", "is_enchanted": false, "level": "30"}, {"artifact_id": "Artifact16", "is_enchanted": false, "level": "30"}, {"artifact_id": "Artifact17", "is_enchanted": true, "level": "4.32277588800000E+95"}, {"artifact_id": "Artifact18", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact19", "is_enchanted": true, "level": "2.48044355500000E+102"}, {"artifact_id": "Artifact2", "is_enchanted": true, "level": "2.96255466600000E+102"}, {"artifact_id": "Artifact20", "is_enchanted": true, "level": "4.54276588800000E+89"}, {"artifact_id": "Artifact21", "is_enchanted": false, "level": "50"}, {"artifact_id": "Artifact22", "is_enchanted": true, "level": "2.67074024000000E+81"}, {"artifact_id": "Artifact23", "is_enchanted": true, "level": "4.32277588800000E+95"}, {"artifact_id": "Artifact24", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact25", "is_enchanted": true, "level": "4.32277588800000E+95"}, {"artifact_id": "Artifact26", "is_enchanted": true, "level": "3.12711112000000E+89"}, {"artifact_id": "Artifact27", "is_enchanted": false, "level": "30"}, {"artifact_id": "Artifact28", "is_enchanted": true, "level": "4.32277588800000E+95"}, {"artifact_id": "Artifact29", "is_enchanted": true, "level": "1.82033244400000E+106"}, {"artifact_id": "Artifact3", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact30", "is_enchanted": true, "level": "7.05175268000000E+92"}, {"artifact_id": "Artifact31", "is_enchanted": true, "level": "3.75266577700000E+95"}, {"artifact_id": "Artifact32", "is_enchanted": true, "level": "1.72133233300000E+106"}, {"artifact_id": "Artifact33", "is_enchanted": true, "level": "1.72133233300000E+106"}, {"artifact_id": "Artifact34", "is_enchanted": true, "level": "1.72133233300000E+106"}, {"artifact_id": "Artifact35", "is_enchanted": true, "level": "1.72133233300000E+106"}, {"artifact_id": "Artifact36", "is_enchanted": false, "level": "20"}, {"artifact_id": "Artifact37", "is_enchanted": false, "level": "30"}, {"artifact_id": "Artifact38", "is_enchanted": true, "level": "2.70711222000000E+95"}, {"artifact_id": "Artifact39", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact4", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact40", "is_enchanted": true, "level": "4.64277588900000E+89"}, {"artifact_id": "Artifact41", "is_enchanted": true, "level": "1.82033244400000E+106"}, {"artifact_id": "Artifact42", "is_enchanted": true, "level": "1.82033244400000E+106"}, {"artifact_id": "Artifact43", "is_enchanted": true, "level": "2.80454365600000E+102"}, {"artifact_id": "Artifact44", "is_enchanted": true, "level": "2.01453463500000E+102"}, {"artifact_id": "Artifact45", "is_enchanted": true, "level": "1.71511011000000E+102"}, {"artifact_id": "Artifact46", "is_enchanted": true, "level": "1.82033244400000E+106"}, {"artifact_id": "Artifact47", "is_enchanted": true, "level": "2.96255466600000E+102"}, {"artifact_id": "Artifact48", "is_enchanted": false, "level": "30"}, {"artifact_id": "Artifact49", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact5", "is_enchanted": false, "level": "50"}, {"artifact_id": "Artifact50", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact51", "is_enchanted": true, "level": "3.84964694700000E+95"}, {"artifact_id": "Artifact52", "is_enchanted": true, "level": "4.54276588800000E+89"}, {"artifact_id": "Artifact53", "is_enchanted": true, "level": "4.54276588800000E+89"}, {"artifact_id": "Artifact54", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact55", "is_enchanted": true, "level": "3.75266577700000E+95"}, {"artifact_id": "Artifact56", "is_enchanted": true, "level": "3.75266577700000E+95"}, {"artifact_id": "Artifact57", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact58", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact59", "is_enchanted": true, "level": "1.82033244400000E+106"}, {"artifact_id": "Artifact6", "is_enchanted": true, "level": "1.82033244400000E+106"}, {"artifact_id": "Artifact60", "is_enchanted": false, "level": "60"}, {"artifact_id": "Artifact61", "is_enchanted": true, "level": "1.72133233300000E+106"}, {"artifact_id": "Artifact62", "is_enchanted": true, "level": "1.72133233300000E+106"}, {"artifact_id": "Artifact63", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact64", "is_enchanted": true, "level": "2.80454365600000E+102"}, {"artifact_id": "Artifact65", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact66", "is_enchanted": true, "level": "2.80454365600000E+102"}, {"artifact_id": "Artifact67", "is_enchanted": true, "level": "1.82033244400000E+106"}, {"artifact_id": "Artifact68", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact69", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact7", "is_enchanted": true, "level": "1.82033244400000E+106"}, {"artifact_id": "Artifact70", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact71", "is_enchanted": false, "level": "50"}, {"artifact_id": "Artifact72", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact73", "is_enchanted": true, "level": "4.32277588800000E+95"}, {"artifact_id": "Artifact74", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact75", "is_enchanted": true, "level": "4.64277588900000E+89"}, {"artifact_id": "Artifact76", "is_enchanted": true, "level": "4.64277588900000E+89"}, {"artifact_id": "Artifact77", "is_enchanted": true, "level": "4.64277588900000E+89"}, {"artifact_id": "Artifact78", "is_enchanted": true, "level": "4.64277588900000E+89"}, {"artifact_id": "Artifact79", "is_enchanted": true, "level": "1.47433265400000E+102"}, {"artifact_id": "Artifact8", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact80", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact81", "is_enchanted": false, "level": "40"}, {"artifact_id": "Artifact82", "is_enchanted": true, "level": "2.62255466600000E+102"}, {"artifact_id": "Artifact83", "is_enchanted": true, "level": "3.75266577700000E+95"}, {"artifact_id": "Artifact84", "is_enchanted": true, "level": "3.79511011000000E+89"}, {"artifact_id": "Artifact85", "is_enchanted": false, "level": "50"}, {"artifact_id": "Artifact86", "is_enchanted": true, "level": "4.54276588800000E+89"}, {"artifact_id": "Artifact87", "is_enchanted": true, "level": "4.54276588800000E+89"}, {"artifact_id": "Artifact88", "is_enchanted": true, "level": "4.54276588800000E+89"}, {"artifact_id": "Artifact89", "is_enchanted": true, "level": "4.54276588800000E+89"}, {"artifact_id": "Artifact9", "is_enchanted": true, "level": "1.82033244400000E+106"}, {"artifact_id": "Artifact90", "is_enchanted": true, "level": "4.54276588800000E+89"}, {"artifact_id": "Artifact91", "is_enchanted": false, "level": "50"}, {"artifact_id": "Artifact92", "is_enchanted": false, "level": "50"}, {"artifact_id": "Artifact93", "is_enchanted": false, "level": "50"}, {"artifact_id": "Artifact94", "is_enchanted": true, "level": "4.76277699900000E+89"}, {"artifact_id": "Artifact95", "is_enchanted": true, "level": "2.97255466600000E+102"}, {"artifact_id": "Artifact96", "is_enchanted": true, "level": "4.54276588800000E+89"}, {"artifact_id": "Artifact97", "is_enchanted": true, "level": "4.54276588800000E+89"}, {"artifact_id": "Artifact98", "is_enchanted": true, "level": "7.05175268000000E+92"}, {"artifact_id": "Artifact99", "is_enchanted": true, "level": "7.05175268000000E+92"}], "badge_count": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 47}, "cards": [{"level": 46, "quantity_received": 4392, "quantity_spent": 4392, "skill_name": "AstralEcho"}, {"level": 44, "quantity_received": 6733, "quantity_spent": 6471, "skill_name": "BurningAttack"}, {"level": 47, "quantity_received": 7278, "quantity_spent": 7272, "skill_name": "BurstBoost"}, {"level": 45, "quantity_received": 6990, "quantity_spent": 6750, "skill_name": "BurstCount"}, {"level": 45, "quantity_received": 3632, "quantity_spent": 3506, "skill_name": "CelestialStatic"}, {"level": 47, "quantity_received": 7476, "quantity_spent": 7402, "skill_name": "ChainLightning"}, {"level": 51, "quantity_received": 8451, "quantity_spent": 8364, "skill_name": "CrushingVoid"}, {"level": 46, "quantity_received": 7330, "quantity_spent": 7230, "skill_name": "DecayingAttack"}, {"level": 45, "quantity_received": 6588, "quantity_spent": 6344, "skill_name": "Disease"}, {"level": 46, "quantity_received": 6806, "quantity_spent": 6611, "skill_name": "ExecutionersAxe"}, {"level": 47, "quantity_received": 7178, "quantity_spent": 7177, "skill_name": "FinisherAttack"}, {"level": 45, "quantity_received": 6799, "quantity_spent": 6799, "skill_name": "FlakShot"}, {"level": 46, "quantity_received": 6638, "quantity_spent": 6612, "skill_name": "Fragmentize"}, {"level": 47, "quantity_received": 7439, "quantity_spent": 7313, "skill_name": "Fuse"}, {"level": 46, "quantity_received": 6995, "quantity_spent": 6928, "skill_name": "Haymaker"}, {"level": 45, "quantity_received": 6509, "quantity_spent": 6501, "skill_name": "ImpactAttack"}, {"level": 46, "quantity_received": 6762, "quantity_spent": 6595, "skill_name": "InnerTruth"}, {"level": 46, "quantity_received": 7265, "quantity_spent": 7217, "skill_name": "LimbBurst"}, {"level": 47, "quantity_received": 7497, "quantity_spent": 7460, "skill_name": "LimbSupport"}, {"level": 46, "quantity_received": 7082, "quantity_spent": 6927, "skill_name": "MentalFocus"}, {"level": 49, "quantity_received": 4600, "quantity_spent": 4486, "skill_name": "MirrorForce"}, {"level": 45, "quantity_received": 6729, "quantity_spent": 6647, "skill_name": "MoonBeam"}, {"level": 46, "quantity_received": 7281, "quantity_spent": 7049, "skill_name": "PlagueAttack"}, {"level": 45, "quantity_received": 5865, "quantity_spent": 5753, "skill_name": "PoisonAttack"}, {"level": 45, "quantity_received": 4428, "quantity_spent": 4361, "skill_name": "PowerBubble"}, {"level": 49, "quantity_received": 8361, "quantity_spent": 8047, "skill_name": "Purify"}, {"level": 45, "quantity_received": 5976, "quantity_spent": 5846, "skill_name": "RazorWind"}, {"level": 49, "quantity_received": 4616, "quantity_spent": 4557, "skill_name": "RuinousRust"}, {"level": 49, "quantity_received": 8570, "quantity_spent": 8382, "skill_name": "RuneAttack"}, {"level": 45, "quantity_received": 6752, "quantity_spent": 6699, "skill_name": "Shadow"}, {"level": 45, "quantity_received": 6347, "quantity_spent": 6300, "skill_name": "SkullBash"}, {"level": 49, "quantity_received": 4654, "quantity_spent": 4337, "skill_name": "SpinalTap"}, {"level": 46, "quantity_received": 7166, "quantity_spent": 6989, "skill_name": "SuperheatMetal"}, {"level": 49, "quantity_received": 8339, "quantity_spent": 8103, "skill_name": "Swarm"}, {"level": 46, "quantity_received": 7138, "quantity_spent": 6952, "skill_name": "TeamTactics"}, {"level": 51, "quantity_received": 8996, "quantity_spent": 8954, "skill_name": "TotemFairySkill"}, {"level": 48, "quantity_received": 7980, "quantity_spent": 7720, "skill_name": "WhipOfLightning"}], "challenge_tournaments_participation": "151", "challenge_tournaments_undisputed_count": "0", "clan_code": "vg9e2", "clan_name": "TapTitanUniverse", "clan_scroll": [{"Level": 503, "ScrollId": "ScrollId6"}, {"Level": 503, "ScrollId": "ScrollId4"}, {"Level": 503, "ScrollId": "ScrollId8"}, {"Level": 506, "ScrollId": "ScrollId17"}, {"Level": 504, "ScrollId": "ScrollId5"}, {"Level": 505, "ScrollId": "ScrollId2"}, {"Level": 503, "ScrollId": "ScrollId13"}, {"Level": 506, "ScrollId": "ScrollId16"}, {"Level": 502, "ScrollId": "ScrollId7"}, {"Level": 503, "ScrollId": "ScrollId15"}, {"Level": 503, "ScrollId": "ScrollId1"}, {"Level": 503, "ScrollId": "ScrollId18"}, {"Level": 505, "ScrollId": "ScrollId12"}, {"Level": 504, "ScrollId": "ScrollId3"}, {"Level": 503, "ScrollId": "ScrollId11"}, {"Level": 506, "ScrollId": "ScrollId10"}, {"Level": 503, "ScrollId": "ScrollId9"}, {"Level": 503, "ScrollId": "ScrollId14"}], "country_code": "US", "crafting_shards_spent": 74604, "current_card_currency": 2735, "current_world_id": "59", "daily_raid_tickets": "64559", "equipment_set": ["Gingerbread", "MultiCast", "Gamer", "AnniversaryFairy", "Bishop", "Samurai", "Anniversary", "Sled", "Snowman", "Grill", "Dancer", "Enchant", "Maple", "Ninja", "Twilight", "GoldAngel", "Picnic", "Surf", "BlueFlame", "Dungeoneer", "Zeus", "LifetimePrestige", "ElectricWarlord", "Ninetails", "Wonder", "Beach", "MetallicLightning", "Chakram", "Cowboy", "ShadowMagician", "Chains", "Cyborg", "Jukk", "Headless", "RaidCaptain", "Blacksmith", "Ghost", "Medic", "Nomad", "Pyro", "Knight", "Tank", "Titan", "CNY", "LightBunny", "Pharaoh", "BlueKnight", "Vampire", "ManaMage", "Devil", "FireTribe", "BlackDragon", "Lifeguard", "Baker", "Fur", "HighTecLightning", "PetChampion", "DOS", "ScrollMaster", "WaterSorcerer", "WeaponMaster", "Lolita", "Damon", "Green", "Demon", "GoldRain", "Captain", "Diamond", "Bazooka", "Lance", "DarkAlien", "FirstMate", "Rosabella", "TimeWizard", "Spacesuit", "WarHorn", "Musketeer", "Kronus", "Witch", "FairyShaman", "Monk", "DarkAngel", "Jayce", "Thief", "GoldGun", "Quinn", "Sophia", "Skulls", "SteampunkKnight", "Prestigious", "Gambler", "Reaper", "Platinum", "RaidMythic", "Gulbrand", "Jade", "WildCat", "Bard", "Rockstar", "BoneTribe", "FireKnight", "DaggerRogue", "Snowboard", "Midas", "Mage", "Dragon", "Frost", "Viking", "Poet", "TwilightFairyKing", "Cupid", "AlphaHeart", "Slayer", "Sports", "ElderSnow", "FireCook", "Aquamarine", "Hunter", "Crow", "EarthRogue", "Punk", "SunBather", "Influencer", "Sun", "PetTamer", "Shepherd", "Jester", "SpaceKnight", "FairyKnight", "Scientist", "Scarecrow", "Grinch", "Pirate", "Titania", "PerkMaster", "Hollow", "Yeti", "Spellmaster", "SpellBooster", "Scout", "Corrupted", "Bane", "AirshipEngineer", "Spartan", "SoloRaid", "Wolf", "Stone", "RockGirl", "Mech", "PlagueDoctor", "Rogue"], "equipment_set_count": "151", "hero_weapon": [{"HelperID": "H26", "Level": 307}, {"HelperID": "H04", "Level": 307}, {"HelperID": "H24", "Level": 307}, {"HelperID": "H30", "Level": 308}, {"HelperID": "H12", "Level": 308}, {"HelperID": "H15", "Level": 308}, {"HelperID": "H21", "Level": 307}, {"HelperID": "H31", "Level": 308}, {"HelperID": "H28", "Level": 307}, {"HelperID": "H34", "Level": 308}, {"HelperID": "H13", "Level": 307}, {"HelperID": "H25", "Level": 307}, {"HelperID": "H11", "Level": 307}, {"HelperID": "H08", "Level": 308}, {"HelperID": "H05", "Level": 307}, {"HelperID": "H10", "Level": 307}, {"HelperID": "H02", "Level": 307}, {"HelperID": "H06", "Level": 307}, {"HelperID": "H14", "Level": 313}, {"HelperID": "H03", "Level": 308}, {"HelperID": "H07", "Level": 308}, {"HelperID": "H29", "Level": 307}, {"HelperID": "H01", "Level": 307}, {"HelperID": "H23", "Level": 309}, {"HelperID": "H17", "Level": 308}, {"HelperID": "H20", "Level": 307}, {"HelperID": "H35", "Level": 307}, {"HelperID": "H16", "Level": 307}, {"HelperID": "H36", "Level": 310}, {"HelperID": "H09", "Level": 307}, {"HelperID": "H19", "Level": 308}, {"HelperID": "H32", "Level": 307}, {"HelperID": "H33", "Level": 308}, {"HelperID": "H22", "Level": 308}, {"HelperID": "H18", "Level": 307}, {"HelperID": "H37", "Level": 307}, {"HelperID": "H27", "Level": 307}], "loyalty_level": "12", "max_stage": 337995, "name": "pizza toppings", "pets": [{"level": 2436, "pet_id": "Pet1"}, {"level": 2207, "pet_id": "Pet10"}, {"level": 2168, "pet_id": "Pet11"}, {"level": 2397, "pet_id": "Pet12"}, {"level": 2199, "pet_id": "Pet13"}, {"level": 2144, "pet_id": "Pet14"}, {"level": 2357, "pet_id": "Pet15"}, {"level": 2320, "pet_id": "Pet16"}, {"level": 1394, "pet_id": "Pet17"}, {"level": 1338, "pet_id": "Pet18"}, {"level": 1510, "pet_id": "Pet19"}, {"level": 2370, "pet_id": "Pet2"}, {"level": 1579, "pet_id": "Pet20"}, {"level": 1624, "pet_id": "Pet21"}, {"level": 1487, "pet_id": "Pet22"}, {"level": 1477, "pet_id": "Pet23"}, {"level": 1464, "pet_id": "Pet24"}, {"level": 1471, "pet_id": "Pet25"}, {"level": 1583, "pet_id": "Pet26"}, {"level": 1505, "pet_id": "Pet27"}, {"level": 1611, "pet_id": "Pet28"}, {"level": 1348, "pet_id": "Pet29"}, {"level": 2274, "pet_id": "Pet3"}, {"level": 1447, "pet_id": "Pet30"}, {"level": 2199, "pet_id": "Pet4"}, {"level": 2270, "pet_id": "Pet5"}, {"level": 2526, "pet_id": "Pet6"}, {"level": 2706, "pet_id": "Pet7"}, {"level": 2521, "pet_id": "Pet8"}, {"level": 2167, "pet_id": "Pet9"}, {"level": 389, "pet_id": "SeasonalPet4"}, {"level": 391, "pet_id": "SeasonalPet10"}, {"level": 402, "pet_id": "SeasonalPet8"}, {"level": 370, "pet_id": "SeasonalPet6"}, {"level": 397, "pet_id": "SeasonalPet5"}, {"level": 390, "pet_id": "SeasonalPet3"}, {"level": 379, "pet_id": "SeasonalPet9"}, {"level": 390, "pet_id": "SeasonalPet7"}, {"level": 389, "pet_id": "SeasonalPet2"}, {"level": 399, "pet_id": "SeasonalPet1"}], "player_code": "pqge37k", "player_raid_level": "1132", "previous_rank": "0.0679", "raid_wildcard_count": 39, "relics_received": "9.39561737348372E+287", "relics_spent": "9.33643670525163E+287", "role": "CoLeaderAdmin", "seasonal_artifacts": [{"artifact_id": "SeasonalArtifact1", "is_enchanted": false, "level": "32.0000000000000"}, {"artifact_id": "SeasonalArtifact10", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact15", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact16", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact18", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact19", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact2", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact20", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact22", "is_enchanted": false, "level": "34.0000000000000"}, {"artifact_id": "SeasonalArtifact3", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact34", "is_enchanted": false, "level": "13000.0000000000"}, {"artifact_id": "SeasonalArtifact35", "is_enchanted": false, "level": "13000.0000000000"}, {"artifact_id": "SeasonalArtifact36", "is_enchanted": false, "level": "32.0000000000000"}, {"artifact_id": "SeasonalArtifact38", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact39", "is_enchanted": false, "level": "13000.0000000000"}, {"artifact_id": "SeasonalArtifact4", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact40", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact42", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact43", "is_enchanted": false, "level": "12000.0000000000"}, {"artifact_id": "SeasonalArtifact7", "is_enchanted": false, "level": "33.0000000000000"}, {"artifact_id": "SeasonalArtifact9", "is_enchanted": false, "level": "33.0000000000000"}], "seasonal_relic_multiplier": 1700, "seasonal_relics_received": "5708633938519830000000000000", "seasonal_relics_spent": "5691381588622030000000000000", "skill_tree": [{"level": 27, "skill_id": "TapDmg"}, {"level": 25, "skill_id": "TapDmgFromHelpers"}, {"level": 1, "skill_id": "FairyGold"}, {"level": 25, "skill_id": "HeavyStrikes"}, {"level": 9, "skill_id": "FairyChance"}, {"level": 20, "skill_id": "Frenzy"}, {"level": 28, "skill_id": "PetDmg"}, {"level": 25, "skill_id": "FireTapSkillBoost"}, {"level": 21, "skill_id": "PetGoldQTE"}, {"level": 29, "skill_id": "PetEquipmentBoost"}, {"level": 30, "skill_id": "PetBonusBoost"}, {"level": 29, "skill_id": "PetQTE"}, {"level": 30, "skill_id": "CombatTechniques"}, {"level": 3, "skill_id": "TapBoostMultiCastSkill"}, {"level": 20, "skill_id": "BossDmgQTE"}, {"level": 20, "skill_id": "DualPetBoost"}, {"level": 3, "skill_id": "DualPetMultiCast"}, {"level": 2, "skill_id": "AllHelperDmg"}, {"level": 25, "skill_id": "HelperBoost"}, {"level": 5, "skill_id": "HelperDmgSkillBoost"}, {"level": 1, "skill_id": "ClanShipDmg"}, {"level": 6, "skill_id": "ClanQTE"}, {"level": 7, "skill_id": "HelperInspiredWeaken"}, {"level": 30, "skill_id": "ClanShipStun"}, {"level": 5, "skill_id": "HelperDmgQTE"}, {"level": 2, "skill_id": "HelperBoostMultiCastSkill"}, {"level": 2, "skill_id": "CloneDmg"}, {"level": 10, "skill_id": "MPCapacityBoost"}, {"level": 1, "skill_id": "CloneSkillBoost"}, {"level": 1, "skill_id": "ManaStealSkillBoost"}, {"level": 5, "skill_id": "ManaMonster"}, {"level": 30, "skill_id": "BossTimer"}, {"level": 23, "skill_id": "CritSkillBoost"}, {"level": 20, "skill_id": "ForbiddenContract"}, {"level": 20, "skill_id": "TerrifyingPact"}, {"level": 5, "skill_id": "OfflineGold"}, {"level": 15, "skill_id": "CritSkillBoostDmg"}, {"level": 9, "skill_id": "Cloaking"}, {"level": 25, "skill_id": "Backstab"}, {"level": 10, "skill_id": "MultiMonsters"}, {"level": 3, "skill_id": "GuidedBlade"}, {"level": 17, "skill_id": "LoadedDice"}, {"level": 7, "skill_id": "Transmutation"}, {"level": 1, "skill_id": "ChestGold"}, {"level": 3, "skill_id": "MidasSkillBoost"}, {"level": 9, "skill_id": "LovePotion"}, {"level": 2, "skill_id": "HandOfMidasMultiCastSkillBoost"}, {"level": 20, "skill_id": "KratosSummon"}, {"level": 17, "skill_id": "RoyalContract"}], "titan_points": "157308", "total_card_level": "1724", "total_clan_scrolls": "9068", "total_helper_weapons": "11382", "total_pet_levels": "58099", "total_raid_player_xp": "1772974", "total_skill_points": "14173", "total_tournaments": "712", "undisputed_count": "406", "weekly_ticket_count": "462"}'''
