from unittest import TestCase

from tap_titans.models import models
from tap_titans.abcs.rest_api import ClanDataResp, SubscribeResp


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

    def test_raid_retire_by_system(self):
        models.raid_models.RaidRetire.decode_json(_raid_retire_by_system)

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

    def test_subscribe(self):
        SubscribeResp.decode_json(_subscribe_data)

    def test_clan_data(self):
        ClanDataResp.decode_json(_clan_data)

    def test_player_data(self):
        models.player_models.PlayerData.decode_json(_player_data)

    def test_clan_kick_optional_executor(self):
        models.clan_models.ClanKick.decode_json(_clan_kick_optional_executor)

    def test_protect_secrets(self):
        start_checking = False
        warnings = []

        for key, value in globals().items():
            if key == self.__class__.__name__:
                start_checking = True
                continue

            if not start_checking:
                continue

            for field, test_cases in [
                    ('player_code', (
                        '"player_code":"test"',
                        '"player_code": "test"',
                        '"player_code":"string"',
                        '"player_code": "string"',
                    )),
                    ('player_name', (
                            '"player_name":"test"',
                            '"player_name": "test"',
                            '"player_name":"string"',
                            '"player_name": "string"',
                    )),
                    ('clan_code', (
                        '"clan_code":"test"',
                        '"clan_code": "test"',
                        '"clan_code": "string"',
                        '"clan_code":"string"',
                    )),
                    ('clan_name', (
                            '"clan_name":"test"',
                            '"clan_name": "test"',
                            '"clan_name": "string"',
                            '"clan_name":"string"',
                    )),
            ]:
                if field in value and all(test_case not in value for test_case in test_cases):
                    self.fail(f"{field} found in {key} and is missing obfuscation")


_raid_start = '''{"clan_code": "test", "keys_remaining": 1,
               "morale": {"bonus_amount": 0.25, "used": 0},
               "player": {"name": "test", "player_code": "test"},
               "raid": {"area_buffs": [{"bonus_amount": 3.0, "bonus_type": "RaidAttackDuration"}], "level": "1",
                        "spawn_sequence": ["Jukk", "Sterl", "Takedar"], "tier": "9999", "titans": [
                       {"area_debuffs": [{"bonus_amount": 0.5, "bonus_type": "AllLimbsHPMult"}], "enemy_id": "Enemy2",
                        "enemy_name": "Takedar", "parts": [{"part_id": "BodyHead", "total_hp": 1468800000.000001},
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

_raid_retire_by_system = '''{
    "clan_code": "string",
    "raid_id": 0,
    "retired_at": "2019-08-24T14:15:22Z",
    "player": {},
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

_subscribe_data = '''{"ok": [{"clan_code": "test", "clan_name": "test", "member_list": [{"name": "test", "player_code": "test"}], "token": "test"}], "refused": []}'''

_clan_data = '''{"clan_code": "test", "clan_name": "test", "players_data": [{"cards": [{"level": 41, "quantity_received": 3366, "quantity_spent": 3198, "skill_name": "AstralEcho"}, {"level": 37, "quantity_received": 4089, "quantity_spent": 3839, "skill_name": "BurningAttack"}, {"level": 42, "quantity_received": 4503, "quantity_spent": 4077, "skill_name": "BurstBoost"}, {"level": 34, "quantity_received": 3587, "quantity_spent": 3558, "skill_name": "BurstCount"}, {"level": 41, "quantity_received": 3046, "quantity_spent": 2809, "skill_name": "CelestialStatic"}, {"level": 38, "quantity_received": 4212, "quantity_spent": 3813, "skill_name": "ChainLightning"}, {"level": 33, "quantity_received": 3501, "quantity_spent": 3286, "skill_name": "CrushingVoid"}, {"level": 29, "quantity_received": 3430, "quantity_spent": 3298, "skill_name": "DecayingAttack"}, {"level": 35, "quantity_received": 3727, "quantity_spent": 3595, "skill_name": "Disease"}, {"level": 36, "quantity_received": 3769, "quantity_spent": 3639, "skill_name": "ExecutionersAxe"}, {"level": 30, "quantity_received": 2961, "quantity_spent": 2828, "skill_name": "FinisherAttack"}, {"level": 29, "quantity_received": 3260, "quantity_spent": 3133, "skill_name": "FlakShot"}, {"level": 31, "quantity_received": 3171, "quantity_spent": 3092, "skill_name": "Fragmentize"}, {"level": 31, "quantity_received": 3907, "quantity_spent": 3590, "skill_name": "Fuse"}, {"level": 34, "quantity_received": 4115, "quantity_spent": 3870, "skill_name": "Haymaker"}, {"level": 32, "quantity_received": 3502, "quantity_spent": 3418, "skill_name": "ImpactAttack"}, {"level": 31, "quantity_received": 3263, "quantity_spent": 3099, "skill_name": "InnerTruth"}, {"level": 28, "quantity_received": 3522, "quantity_spent": 3223, "skill_name": "LimbBurst"}, {"level": 32, "quantity_received": 3608, "quantity_spent": 3445, "skill_name": "LimbSupport"}, {"level": 51, "quantity_received": 2390, "quantity_spent": 2389, "skill_name": "MagicPotion"}, {"level": 39, "quantity_received": 4084, "quantity_spent": 4046, "skill_name": "MentalFocus"}, {"level": 45, "quantity_received": 4523, "quantity_spent": 4103, "skill_name": "MirrorForce"}, {"level": 32, "quantity_received": 3645, "quantity_spent": 3499, "skill_name": "MoonBeam"}, {"level": 34, "quantity_received": 3873, "quantity_spent": 3675, "skill_name": "PlagueAttack"}, {"level": 25, "quantity_received": 3051, "quantity_spent": 2788, "skill_name": "PoisonAttack"}, {"level": 32, "quantity_received": 2708, "quantity_spent": 2426, "skill_name": "PowerBubble"}, {"level": 51, "quantity_received": 6363, "quantity_spent": 5749, "skill_name": "Purify"}, {"level": 34, "quantity_received": 4081, "quantity_spent": 4048, "skill_name": "RazorWind"}, {"level": 42, "quantity_received": 5107, "quantity_spent": 4655, "skill_name": "RuinousRust"}, {"level": 32, "quantity_received": 3047, "quantity_spent": 2900, "skill_name": "RuneAttack"}, {"level": 23, "quantity_received": 225, "quantity_spent": 225, "skill_name": "SandsOfTime"}, {"level": 37, "quantity_received": 3876, "quantity_spent": 3783, "skill_name": "Shadow"}, {"level": 28, "quantity_received": 3301, "quantity_spent": 3084, "skill_name": "SkullBash"}, {"level": 37, "quantity_received": 4043, "quantity_spent": 3786, "skill_name": "SpinalTap"}, {"level": 34, "quantity_received": 3768, "quantity_spent": 3731, "skill_name": "SuperheatMetal"}, {"level": 31, "quantity_received": 3131, "quantity_spent": 3102, "skill_name": "Swarm"}, {"level": 37, "quantity_received": 4170, "quantity_spent": 4088, "skill_name": "TeamTactics"}, {"level": 50, "quantity_received": 6295, "quantity_spent": 5791, "skill_name": "TotemFairySkill"}, {"level": 33, "quantity_received": 1430, "quantity_spent": 1288, "skill_name": "TriangleSupport"}, {"level": 40, "quantity_received": 253, "quantity_spent": 244, "skill_name": "Weaken"}, {"level": 30, "quantity_received": 3147, "quantity_spent": 2831, "skill_name": "WhipOfLightning"}], "country_code": "UX", "current_card_currency": 0, "daily_raid_tickets": 62253, "loyalty_level": 12, "max_stage": 444667, "name": "test", "player_code": "test", "player_raid_level": 986, "previous_rank": "0.508", "raid_research_bonuses": {"AfflictionBaseDamage": 100.0, "ArmorBaseDamage": 100.0, "BodyBaseDamage": 100.0, "BurstBaseDamage": 100.0, "Enemy1AfflictionBaseDamage": 54.0, "Enemy1BaseDamage": 60.0, "Enemy1BurstBaseDamage": 54.0, "Enemy2AfflictionBaseDamage": 54.0, "Enemy2BaseDamage": 60.0, "Enemy2BurstBaseDamage": 54.0, "Enemy3AfflictionBaseDamage": 54.0, "Enemy3BaseDamage": 60.0, "Enemy3BurstBaseDamage": 54.0, "Enemy4AfflictionBaseDamage": 54.0, "Enemy4BaseDamage": 60.0, "Enemy4BurstBaseDamage": 54.0, "Enemy5AfflictionBaseDamage": 30.0, "Enemy5BaseDamage": 60.0, "Enemy5BurstBaseDamage": 54.0, "Enemy6AfflictionBaseDamage": 30.0, "Enemy6BaseDamage": 60.0, "Enemy6BurstBaseDamage": 54.0, "Enemy7AfflictionBaseDamage": 30.0, "Enemy7BaseDamage": 60.0, "Enemy7BurstBaseDamage": 54.0, "Enemy8AfflictionBaseDamage": 30.0, "Enemy8BaseDamage": 60.0, "Enemy8BurstBaseDamage": 54.0, "HeadArmorBaseDamage": 50.0, "HeadBaseDamage": 72.0, "HeadBodyBaseDamage": 50.0, "LimbArmorBaseDamage": 50.0, "LimbBaseDamage": 72.0, "LimbBodyBaseDamage": 50.0, "RaidBaseDamage": 100.0, "TorsoArmorBaseDamage": 50.0, "TorsoBaseDamage": 72.0, "TorsoBodyBaseDamage": 50.0}, "raid_research_tree": {"ArmorDamage": 0.125, "BodyDamage": 0.125, "ChestDamage": 0.1, "HeadDamage": 0.1, "LimbDamage": 0.1}, "raid_wildcard_count": 279, "role": "CoLeader", "summon_level": 266, "total_card_level": "1441", "total_raid_player_xp": 1383614, "weekly_ticket_count": 462}]}'''

_player_data = '''{"additive_relic_multiplier":36799,"artifacts":[{"artifact_id":"Artifact1","is_enchanted":true,"level":"9.00000000000000E+98"},{"artifact_id":"Artifact10","is_enchanted":true,"level":"7.00000000000000E+103"},{"artifact_id":"Artifact100","is_enchanted":true,"level":"6.00000000000000E+103"},{"artifact_id":"Artifact101","is_enchanted":true,"level":"7.98000000000000E+103"},{"artifact_id":"Artifact102","is_enchanted":true,"level":"3.00000000000000E+91"},{"artifact_id":"Artifact103","is_enchanted":true,"level":"1.30000000000000E+84"},{"artifact_id":"Artifact11","is_enchanted":true,"level":"3.00000000000000E+91"},{"artifact_id":"Artifact12","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact13","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact14","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact15","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact16","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact17","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact18","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact19","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact2","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact20","is_enchanted":true,"level":"7.00000000000000E+87"},{"artifact_id":"Artifact21","is_enchanted":false,"level":"50"},{"artifact_id":"Artifact22","is_enchanted":true,"level":"3.56793200000000E+80"},{"artifact_id":"Artifact23","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact24","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact25","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact26","is_enchanted":true,"level":"7.00000000000000E+87"},{"artifact_id":"Artifact27","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact28","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact29","is_enchanted":true,"level":"1.20000000000000E+104"},{"artifact_id":"Artifact3","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact30","is_enchanted":true,"level":"1.10000000000000E+104"},{"artifact_id":"Artifact31","is_enchanted":true,"level":"4.00000000000000E+93"},{"artifact_id":"Artifact32","is_enchanted":true,"level":"1.10000000000000E+104"},{"artifact_id":"Artifact33","is_enchanted":true,"level":"1.10000000000000E+104"},{"artifact_id":"Artifact34","is_enchanted":true,"level":"1.00000000000000E+104"},{"artifact_id":"Artifact35","is_enchanted":true,"level":"1.10000000000000E+104"},{"artifact_id":"Artifact36","is_enchanted":false,"level":"20"},{"artifact_id":"Artifact37","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact38","is_enchanted":true,"level":"4.00000000000000E+93"},{"artifact_id":"Artifact39","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact4","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact40","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact41","is_enchanted":true,"level":"7.00000000000000E+103"},{"artifact_id":"Artifact42","is_enchanted":true,"level":"9.00000000000000E+103"},{"artifact_id":"Artifact43","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact44","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact45","is_enchanted":true,"level":"1.00000000000000E+88"},{"artifact_id":"Artifact46","is_enchanted":true,"level":"9.00000000000000E+103"},{"artifact_id":"Artifact47","is_enchanted":true,"level":"1.50000000000000E+100"},{"artifact_id":"Artifact48","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact49","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact5","is_enchanted":false,"level":"50"},{"artifact_id":"Artifact50","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact51","is_enchanted":true,"level":"2.00000000000000E+93"},{"artifact_id":"Artifact52","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact53","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact54","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact55","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact56","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact57","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact58","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact59","is_enchanted":true,"level":"1.20000000000000E+104"},{"artifact_id":"Artifact6","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact60","is_enchanted":false,"level":"60"},{"artifact_id":"Artifact61","is_enchanted":true,"level":"1.00000000000000E+104"},{"artifact_id":"Artifact62","is_enchanted":true,"level":"1.00000000000000E+104"},{"artifact_id":"Artifact63","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact64","is_enchanted":true,"level":"1.00000000000000E+100"},{"artifact_id":"Artifact65","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact66","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact67","is_enchanted":true,"level":"1.00000000000000E+104"},{"artifact_id":"Artifact68","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact69","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact7","is_enchanted":true,"level":"7.00000000000000E+103"},{"artifact_id":"Artifact70","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"Artifact71","is_enchanted":false,"level":"50.0000000000000"},{"artifact_id":"Artifact72","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"Artifact73","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact74","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"Artifact75","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact76","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact77","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact78","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact79","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact8","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact80","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"Artifact81","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"Artifact82","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact83","is_enchanted":true,"level":"4.00000000000000E+93"},{"artifact_id":"Artifact84","is_enchanted":true,"level":"7.00000000000000E+87"},{"artifact_id":"Artifact85","is_enchanted":false,"level":"50.0000000000000"},{"artifact_id":"Artifact86","is_enchanted":true,"level":"4.00000000000000E+87"},{"artifact_id":"Artifact87","is_enchanted":true,"level":"4.00000000000000E+87"},{"artifact_id":"Artifact88","is_enchanted":true,"level":"4.00000000000000E+87"},{"artifact_id":"Artifact89","is_enchanted":true,"level":"4.00000000000000E+87"},{"artifact_id":"Artifact9","is_enchanted":true,"level":"7.00000000000000E+103"},{"artifact_id":"Artifact90","is_enchanted":true,"level":"4.00000000000000E+87"},{"artifact_id":"Artifact91","is_enchanted":false,"level":"50.0000000000000"},{"artifact_id":"Artifact92","is_enchanted":false,"level":"50.0000000000000"},{"artifact_id":"Artifact93","is_enchanted":false,"level":"50.0000000000000"},{"artifact_id":"Artifact94","is_enchanted":true,"level":"7.00000000000000E+87"},{"artifact_id":"Artifact95","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact96","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact97","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact98","is_enchanted":true,"level":"3.00000000000000E+91"},{"artifact_id":"Artifact99","is_enchanted":true,"level":"3.00000000000000E+91"}],"badge_count":{"0":0,"1":0,"2":20,"3":13,"4":1},"cards":[{"level":41,"quantity_received":3366,"quantity_spent":3198,"skill_name":"AstralEcho"},{"level":37,"quantity_received":4089,"quantity_spent":3839,"skill_name":"BurningAttack"},{"level":42,"quantity_received":4503,"quantity_spent":4077,"skill_name":"BurstBoost"},{"level":34,"quantity_received":3587,"quantity_spent":3558,"skill_name":"BurstCount"},{"level":41,"quantity_received":3046,"quantity_spent":2809,"skill_name":"CelestialStatic"},{"level":38,"quantity_received":4212,"quantity_spent":3813,"skill_name":"ChainLightning"},{"level":33,"quantity_received":3501,"quantity_spent":3286,"skill_name":"CrushingVoid"},{"level":29,"quantity_received":3430,"quantity_spent":3298,"skill_name":"DecayingAttack"},{"level":35,"quantity_received":3727,"quantity_spent":3595,"skill_name":"Disease"},{"level":36,"quantity_received":3769,"quantity_spent":3639,"skill_name":"ExecutionersAxe"},{"level":30,"quantity_received":2961,"quantity_spent":2828,"skill_name":"FinisherAttack"},{"level":29,"quantity_received":3260,"quantity_spent":3133,"skill_name":"FlakShot"},{"level":31,"quantity_received":3171,"quantity_spent":3092,"skill_name":"Fragmentize"},{"level":31,"quantity_received":3907,"quantity_spent":3590,"skill_name":"Fuse"},{"level":34,"quantity_received":4115,"quantity_spent":3870,"skill_name":"Haymaker"},{"level":32,"quantity_received":3502,"quantity_spent":3418,"skill_name":"ImpactAttack"},{"level":31,"quantity_received":3263,"quantity_spent":3099,"skill_name":"InnerTruth"},{"level":28,"quantity_received":3522,"quantity_spent":3223,"skill_name":"LimbBurst"},{"level":32,"quantity_received":3608,"quantity_spent":3445,"skill_name":"LimbSupport"},{"level":51,"quantity_received":2390,"quantity_spent":2389,"skill_name":"MagicPotion"},{"level":39,"quantity_received":4084,"quantity_spent":4046,"skill_name":"MentalFocus"},{"level":45,"quantity_received":4523,"quantity_spent":4103,"skill_name":"MirrorForce"},{"level":32,"quantity_received":3645,"quantity_spent":3499,"skill_name":"MoonBeam"},{"level":34,"quantity_received":3873,"quantity_spent":3675,"skill_name":"PlagueAttack"},{"level":25,"quantity_received":3051,"quantity_spent":2788,"skill_name":"PoisonAttack"},{"level":32,"quantity_received":2708,"quantity_spent":2426,"skill_name":"PowerBubble"},{"level":51,"quantity_received":6363,"quantity_spent":5749,"skill_name":"Purify"},{"level":34,"quantity_received":4081,"quantity_spent":4048,"skill_name":"RazorWind"},{"level":42,"quantity_received":5107,"quantity_spent":4655,"skill_name":"RuinousRust"},{"level":32,"quantity_received":3047,"quantity_spent":2900,"skill_name":"RuneAttack"},{"level":23,"quantity_received":225,"quantity_spent":225,"skill_name":"SandsOfTime"},{"level":37,"quantity_received":3876,"quantity_spent":3783,"skill_name":"Shadow"},{"level":28,"quantity_received":3301,"quantity_spent":3084,"skill_name":"SkullBash"},{"level":37,"quantity_received":4043,"quantity_spent":3786,"skill_name":"SpinalTap"},{"level":34,"quantity_received":3768,"quantity_spent":3731,"skill_name":"SuperheatMetal"},{"level":31,"quantity_received":3131,"quantity_spent":3102,"skill_name":"Swarm"},{"level":37,"quantity_received":4170,"quantity_spent":4088,"skill_name":"TeamTactics"},{"level":50,"quantity_received":6295,"quantity_spent":5791,"skill_name":"TotemFairySkill"},{"level":33,"quantity_received":1430,"quantity_spent":1288,"skill_name":"TriangleSupport"},{"level":40,"quantity_received":253,"quantity_spent":244,"skill_name":"Weaken"},{"level":30,"quantity_received":3147,"quantity_spent":2831,"skill_name":"WhipOfLightning"}],"challenge_tournaments_participation":"126","challenge_tournaments_undisputed_count":"1","clan_code":"test","clan_name":"test","clan_scroll":[{"Level":360,"ScrollId":"ScrollId11"},{"Level":360,"ScrollId":"ScrollId17"},{"Level":362,"ScrollId":"ScrollId12"},{"Level":361,"ScrollId":"ScrollId15"},{"Level":361,"ScrollId":"ScrollId7"},{"Level":363,"ScrollId":"ScrollId6"},{"Level":364,"ScrollId":"ScrollId16"},{"Level":361,"ScrollId":"ScrollId2"},{"Level":360,"ScrollId":"ScrollId9"},{"Level":364,"ScrollId":"ScrollId14"},{"Level":360,"ScrollId":"ScrollId13"},{"Level":359,"ScrollId":"ScrollId3"},{"Level":359,"ScrollId":"ScrollId5"},{"Level":362,"ScrollId":"ScrollId1"},{"Level":359,"ScrollId":"ScrollId8"},{"Level":360,"ScrollId":"ScrollId18"},{"Level":360,"ScrollId":"ScrollId10"},{"Level":360,"ScrollId":"ScrollId4"}],"country_code":"UX","crafting_shards_spent":20580,"current_card_currency":0,"current_world_id":"56","daily_raid_tickets":"62253","equipment_set":["ManaMage","Poet","Slayer","PetChampion","Midas","Surf","Runestone","Fur","BunnyDroid","MultiCast","Skulls","Sun","Titan","Spellmaster","Cowboy","BlueFlame","Gulbrand","Titania","Tank","Scarecrow","Medic","AnniversaryFairy","Tropical","Green","DrunkenHammer","AlphaHeart","Zeus","PerkMaster","Doll","Prestigious","Beach","Enchant","Cyborg","Blacksmith","Greed","Witch","Nomad","DaggerRogue","TimeWizard","SpellBooster","Devil","Padlock","SunBather","Ghost","Bishop","Snowboard","Quinn","Musketeer","Jade","FireTribe","Mage","Demon","Maple","Wolf","Dungeoneer","Reaper","Jukk","Sophia","Picnic","Gamer","ScrollTutor","BlackDragon","BoneTribe","LightBunny","TwilightFairyKing","CNY","OathsBurden","WaterSorcerer","SpaceKnight","Yeti","Retaliator","LifetimePrestige","Spartan","Ninjitsu","Twilight","Spacesuit","Grill","Frost","MetallicLightning","Stone","Captain","Sled","Chakram","Jayce","Bane","RaidCaptain","Anniversary","RaidMythic","FirstMate","PetTamer","Influencer","Rosabella","FairyKnight","WildCat","Dancer","FireCook","Dragon","Meat","DarkAngel","Hunter","Thief","Monk","SoulCatcher","Lolita","Bard","Corrupted","Lance","Vampire","Scientist","ElderSnow","Shepherd","Baker","Hollow","Collector","AirshipEngineer","Gambler","Ninetails","Kronus","Rogue","Headless","Aquamarine","Snowman","Wonder","Lifeguard","Diamond","SnakeOil","GoldRain","TitanSouls","Gundam","GunpowderMage","EarthRogue","Bazooka","PetQueen","Jester","Cupid","PlagueDoctor","Sports","RockGirl","ElectricWarlord","Pirate","Samurai","Ninja","Pharaoh","BlueKnight","GoldGun","Damon","Punk","WeaponMaster","Scout","SoloRaid","TinyTitanTree","Formal","GoldAngel","Grinch","FairyShaman","Knight","SteampunkKnight","Platinum","DOS","FireKnight","HighTecLightning","Gingerbread","ShadowMagician","GoldenMech","ScrollMaster","Mech","Viking","Rockstar","WarHorn","Chains","SteelHero","DarkAlien","Pyro","Crow"],"equipment_set_count":"174","hero_weapon":[{"HelperID":"H16","Level":180},{"HelperID":"H23","Level":181},{"HelperID":"H37","Level":181},{"HelperID":"H09","Level":184},{"HelperID":"H25","Level":182},{"HelperID":"H04","Level":181},{"HelperID":"H27","Level":181},{"HelperID":"H18","Level":184},{"HelperID":"H03","Level":181},{"HelperID":"H29","Level":182},{"HelperID":"H06","Level":180},{"HelperID":"H21","Level":182},{"HelperID":"H05","Level":183},{"HelperID":"H07","Level":181},{"HelperID":"H30","Level":183},{"HelperID":"H33","Level":181},{"HelperID":"H26","Level":183},{"HelperID":"H02","Level":182},{"HelperID":"H11","Level":184},{"HelperID":"H01","Level":180},{"HelperID":"H15","Level":182},{"HelperID":"H10","Level":184},{"HelperID":"H14","Level":181},{"HelperID":"H20","Level":182},{"HelperID":"H32","Level":181},{"HelperID":"H08","Level":182},{"HelperID":"H12","Level":181},{"HelperID":"H31","Level":181},{"HelperID":"H36","Level":182},{"HelperID":"H22","Level":183},{"HelperID":"H34","Level":181},{"HelperID":"H19","Level":187},{"HelperID":"H17","Level":181},{"HelperID":"H13","Level":183},{"HelperID":"H28","Level":182},{"HelperID":"H35","Level":181},{"HelperID":"H24","Level":181}],"loyalty_level":"12","max_stage":444667,"name":"test","pets":[{"level":1186,"pet_id":"Pet1"},{"level":938,"pet_id":"Pet10"},{"level":890,"pet_id":"Pet11"},{"level":900,"pet_id":"Pet12"},{"level":965,"pet_id":"Pet13"},{"level":1005,"pet_id":"Pet14"},{"level":1185,"pet_id":"Pet15"},{"level":929,"pet_id":"Pet16"},{"level":617,"pet_id":"Pet17"},{"level":644,"pet_id":"Pet18"},{"level":632,"pet_id":"Pet19"},{"level":1022,"pet_id":"Pet2"},{"level":649,"pet_id":"Pet20"},{"level":741,"pet_id":"Pet21"},{"level":697,"pet_id":"Pet22"},{"level":670,"pet_id":"Pet23"},{"level":685,"pet_id":"Pet24"},{"level":676,"pet_id":"Pet25"},{"level":711,"pet_id":"Pet26"},{"level":656,"pet_id":"Pet27"},{"level":645,"pet_id":"Pet28"},{"level":635,"pet_id":"Pet29"},{"level":920,"pet_id":"Pet3"},{"level":775,"pet_id":"Pet30"},{"level":913,"pet_id":"Pet4"},{"level":925,"pet_id":"Pet5"},{"level":947,"pet_id":"Pet6"},{"level":1054,"pet_id":"Pet7"},{"level":1031,"pet_id":"Pet8"},{"level":887,"pet_id":"Pet9"},{"level":494,"pet_id":"SeasonalPet1"},{"level":497,"pet_id":"SeasonalPet10"},{"level":480,"pet_id":"SeasonalPet12"},{"level":517,"pet_id":"SeasonalPet15"},{"level":504,"pet_id":"SeasonalPet2"},{"level":505,"pet_id":"SeasonalPet3"},{"level":482,"pet_id":"SeasonalPet4"},{"level":505,"pet_id":"SeasonalPet7"},{"level":496,"pet_id":"SeasonalPet8"},{"level":507,"pet_id":"SeasonalPet9"}],"player_code":"test","player_raid_level":"986","previous_rank":"0.508","raid_research_bonuses":{"AfflictionBaseDamage":100.0,"ArmorBaseDamage":100.0,"BodyBaseDamage":100.0,"BurstBaseDamage":100.0,"Enemy1AfflictionBaseDamage":54.0,"Enemy1BaseDamage":60.0,"Enemy1BurstBaseDamage":54.0,"Enemy2AfflictionBaseDamage":54.0,"Enemy2BaseDamage":60.0,"Enemy2BurstBaseDamage":54.0,"Enemy3AfflictionBaseDamage":54.0,"Enemy3BaseDamage":60.0,"Enemy3BurstBaseDamage":54.0,"Enemy4AfflictionBaseDamage":54.0,"Enemy4BaseDamage":60.0,"Enemy4BurstBaseDamage":54.0,"Enemy5AfflictionBaseDamage":30.0,"Enemy5BaseDamage":60.0,"Enemy5BurstBaseDamage":54.0,"Enemy6AfflictionBaseDamage":30.0,"Enemy6BaseDamage":60.0,"Enemy6BurstBaseDamage":54.0,"Enemy7AfflictionBaseDamage":30.0,"Enemy7BaseDamage":60.0,"Enemy7BurstBaseDamage":54.0,"Enemy8AfflictionBaseDamage":30.0,"Enemy8BaseDamage":60.0,"Enemy8BurstBaseDamage":54.0,"HeadArmorBaseDamage":50.0,"HeadBaseDamage":72.0,"HeadBodyBaseDamage":50.0,"LimbArmorBaseDamage":50.0,"LimbBaseDamage":72.0,"LimbBodyBaseDamage":50.0,"RaidBaseDamage":100.0,"TorsoArmorBaseDamage":50.0,"TorsoBaseDamage":72.0,"TorsoBodyBaseDamage":50.0},"raid_research_tree":{"ArmorDamage":0.125,"BodyDamage":0.125,"ChestDamage":0.1,"HeadDamage":0.1,"LimbDamage":0.1},"raid_wildcard_count":279,"relics_received":"2.89400666364749E+282","relics_spent":"8.94261436670921E+281","role":"CoLeader","seasonal_artifacts":[{"artifact_id":"SeasonalArtifact1","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"SeasonalArtifact10","is_enchanted":false,"level":"38000.0000000000"},{"artifact_id":"SeasonalArtifact14","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact15","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact16","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact17","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact19","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact2","is_enchanted":false,"level":"38000.0000000000"},{"artifact_id":"SeasonalArtifact20","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact21","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact22","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"SeasonalArtifact3","is_enchanted":false,"level":"38000.0000000000"},{"artifact_id":"SeasonalArtifact34","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact35","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact36","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"SeasonalArtifact37","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact38","is_enchanted":false,"level":"38000.0000000000"},{"artifact_id":"SeasonalArtifact39","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact4","is_enchanted":false,"level":"41000.0000000000"},{"artifact_id":"SeasonalArtifact40","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact41","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact42","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact43","is_enchanted":false,"level":"35000.0000000000"},{"artifact_id":"SeasonalArtifact5","is_enchanted":false,"level":"38000.0000000000"},{"artifact_id":"SeasonalArtifact6","is_enchanted":false,"level":"38000.0000000000"},{"artifact_id":"SeasonalArtifact7","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"SeasonalArtifact8","is_enchanted":false,"level":"38000.0000000000"},{"artifact_id":"SeasonalArtifact9","is_enchanted":false,"level":"40.0000000000000"}],"seasonal_relic_multiplier":2555,"seasonal_relics_received":"134508899921468000000000000000000000000000000","seasonal_relics_spent":"80407859807757400000000000000000000000000000","skill_tree":[{"level":4,"skill_id":"TapDmg"},{"level":4,"skill_id":"TapDmgFromHelpers"},{"level":1,"skill_id":"BurstSkillBoost"},{"level":1,"skill_id":"FairyGold"},{"level":17,"skill_id":"HeavyStrikes"},{"level":9,"skill_id":"FairyChance"},{"level":2,"skill_id":"PetDmg"},{"level":5,"skill_id":"PetGoldQTE"},{"level":25,"skill_id":"PetEquipmentBoost"},{"level":30,"skill_id":"CombatTechniques"},{"level":9,"skill_id":"AllHelperDmg"},{"level":23,"skill_id":"HelperBoost"},{"level":12,"skill_id":"HelperDmgSkillBoost"},{"level":31,"skill_id":"ClanShipDmg"},{"level":13,"skill_id":"ClanQTE"},{"level":16,"skill_id":"HelperInspiredWeaken"},{"level":30,"skill_id":"ClanShipStun"},{"level":13,"skill_id":"HelperDmgQTE"},{"level":3,"skill_id":"HelperBoostMultiCastSkill"},{"level":18,"skill_id":"ClanShipVoltage"},{"level":3,"skill_id":"ClanShipVoltageMultiCastSkill"},{"level":2,"skill_id":"CloneDmg"},{"level":5,"skill_id":"MPCapacityBoost"},{"level":1,"skill_id":"CloneSkillBoost"},{"level":1,"skill_id":"ManaStealSkillBoost"},{"level":1,"skill_id":"ManaMonster"},{"level":20,"skill_id":"BossTimer"},{"level":8,"skill_id":"CritSkillBoost"},{"level":20,"skill_id":"ForbiddenContract"},{"level":20,"skill_id":"TerrifyingPact"},{"level":2,"skill_id":"OfflineGold"},{"level":4,"skill_id":"CritSkillBoostDmg"},{"level":1,"skill_id":"UltraDagger"},{"level":9,"skill_id":"Cloaking"},{"level":14,"skill_id":"Backstab"},{"level":30,"skill_id":"PoisonedBlade"},{"level":4,"skill_id":"MultiMonsters"},{"level":2,"skill_id":"GuidedBlade"},{"level":10,"skill_id":"LoadedDice"},{"level":4,"skill_id":"Transmutation"},{"level":6,"skill_id":"ChestGold"},{"level":6,"skill_id":"MidasSkillBoost"},{"level":9,"skill_id":"LovePotion"},{"level":2,"skill_id":"HandOfMidasMultiCastSkillBoost"},{"level":20,"skill_id":"KratosSummon"},{"level":13,"skill_id":"RoyalContract"}],"summon_level":266,"titan_cards":[{"level":35,"quantity_received":125,"quantity_spent":120,"titan_id":"Titan85"},{"level":35,"quantity_received":94,"quantity_spent":90,"titan_id":"Titan119"},{"level":36,"quantity_received":129,"quantity_spent":127,"titan_id":"Titan81"},{"level":34,"quantity_received":113,"quantity_spent":113,"titan_id":"Titan83"},{"level":32,"quantity_received":104,"quantity_spent":100,"titan_id":"Titan88"},{"level":36,"quantity_received":129,"quantity_spent":127,"titan_id":"Titan90"},{"level":35,"quantity_received":122,"quantity_spent":120,"titan_id":"Titan89"},{"level":33,"quantity_received":82,"quantity_spent":80,"titan_id":"Titan104"},{"level":34,"quantity_received":87,"quantity_spent":85,"titan_id":"Titan113"},{"level":33,"quantity_received":80,"quantity_spent":80,"titan_id":"Titan110"},{"level":34,"quantity_received":87,"quantity_spent":85,"titan_id":"Titan102"},{"level":33,"quantity_received":80,"quantity_spent":80,"titan_id":"Titan106"},{"level":32,"quantity_received":104,"quantity_spent":100,"titan_id":"Titan97"},{"level":32,"quantity_received":76,"quantity_spent":75,"titan_id":"Titan114"},{"level":29,"quantity_received":66,"quantity_spent":63,"titan_id":"Titan115"},{"level":32,"quantity_received":78,"quantity_spent":75,"titan_id":"Titan105"},{"level":36,"quantity_received":132,"quantity_spent":127,"titan_id":"Titan95"},{"level":32,"quantity_received":77,"quantity_spent":75,"titan_id":"Titan103"},{"level":30,"quantity_received":70,"quantity_spent":67,"titan_id":"Titan107"},{"level":32,"quantity_received":76,"quantity_spent":75,"titan_id":"Titan109"},{"level":32,"quantity_received":79,"quantity_spent":75,"titan_id":"Titan108"},{"level":33,"quantity_received":81,"quantity_spent":80,"titan_id":"Titan116"},{"level":38,"quantity_received":149,"quantity_spent":142,"titan_id":"Titan93"},{"level":40,"quantity_received":406,"quantity_spent":389,"titan_id":"Titan50"},{"level":38,"quantity_received":354,"quantity_spent":339,"titan_id":"Titan71"},{"level":36,"quantity_received":127,"quantity_spent":127,"titan_id":"Titan96"},{"level":38,"quantity_received":351,"quantity_spent":339,"titan_id":"Titan73"},{"level":40,"quantity_received":394,"quantity_spent":389,"titan_id":"Titan45"},{"level":38,"quantity_received":107,"quantity_spent":106,"titan_id":"Titan100"},{"level":32,"quantity_received":79,"quantity_spent":75,"titan_id":"Titan118"},{"level":38,"quantity_received":346,"quantity_spent":339,"titan_id":"Titan61"},{"level":35,"quantity_received":122,"quantity_spent":120,"titan_id":"Titan92"},{"level":40,"quantity_received":386,"quantity_spent":379,"titan_id":"Titan67"},{"level":40,"quantity_received":383,"quantity_spent":379,"titan_id":"Titan63"},{"level":42,"quantity_received":437,"quantity_spent":422,"titan_id":"Titan77"},{"level":39,"quantity_received":385,"quantity_spent":368,"titan_id":"Titan39"},{"level":32,"quantity_received":79,"quantity_spent":75,"titan_id":"Titan117"},{"level":47,"quantity_received":862,"quantity_spent":839,"titan_id":"Titan27"},{"level":47,"quantity_received":843,"quantity_spent":839,"titan_id":"Titan12"},{"level":38,"quantity_received":358,"quantity_spent":339,"titan_id":"Titan62"},{"level":39,"quantity_received":363,"quantity_spent":359,"titan_id":"Titan65"},{"level":38,"quantity_received":364,"quantity_spent":348,"titan_id":"Titan32"},{"level":35,"quantity_received":125,"quantity_spent":120,"titan_id":"Titan98"},{"level":38,"quantity_received":365,"quantity_spent":348,"titan_id":"Titan53"},{"level":41,"quantity_received":413,"quantity_spent":411,"titan_id":"Titan57"},{"level":38,"quantity_received":352,"quantity_spent":339,"titan_id":"Titan64"},{"level":41,"quantity_received":405,"quantity_spent":400,"titan_id":"Titan72"},{"level":40,"quantity_received":410,"quantity_spent":389,"titan_id":"Titan47"},{"level":47,"quantity_received":859,"quantity_spent":839,"titan_id":"Titan2"},{"level":38,"quantity_received":360,"quantity_spent":348,"titan_id":"Titan51"},{"level":47,"quantity_received":883,"quantity_spent":839,"titan_id":"Titan13"},{"level":47,"quantity_received":846,"quantity_spent":839,"titan_id":"Titan25"},{"level":41,"quantity_received":420,"quantity_spent":400,"titan_id":"Titan78"},{"level":36,"quantity_received":128,"quantity_spent":127,"titan_id":"Titan86"},{"level":39,"quantity_received":155,"quantity_spent":150,"titan_id":"Titan94"},{"level":46,"quantity_received":810,"quantity_spent":795,"titan_id":"Titan1"},{"level":39,"quantity_received":379,"quantity_spent":368,"titan_id":"Titan31"},{"level":40,"quantity_received":396,"quantity_spent":389,"titan_id":"Titan42"},{"level":39,"quantity_received":383,"quantity_spent":368,"titan_id":"Titan52"},{"level":39,"quantity_received":379,"quantity_spent":368,"titan_id":"Titan41"},{"level":40,"quantity_received":389,"quantity_spent":389,"titan_id":"Titan44"},{"level":39,"quantity_received":373,"quantity_spent":368,"titan_id":"Titan34"},{"level":48,"quantity_received":895,"quantity_spent":886,"titan_id":"Titan17"},{"level":38,"quantity_received":364,"quantity_spent":348,"titan_id":"Titan35"},{"level":36,"quantity_received":128,"quantity_spent":127,"titan_id":"Titan82"},{"level":31,"quantity_received":74,"quantity_spent":71,"titan_id":"Titan112"},{"level":41,"quantity_received":406,"quantity_spent":400,"titan_id":"Titan76"},{"level":50,"quantity_received":999,"quantity_spent":990,"titan_id":"Titan10"},{"level":39,"quantity_received":387,"quantity_spent":368,"titan_id":"Titan49"},{"level":40,"quantity_received":385,"quantity_spent":379,"titan_id":"Titan74"},{"level":47,"quantity_received":863,"quantity_spent":839,"titan_id":"Titan14"},{"level":35,"quantity_received":123,"quantity_spent":120,"titan_id":"Titan87"},{"level":39,"quantity_received":362,"quantity_spent":359,"titan_id":"Titan75"},{"level":37,"quantity_received":338,"quantity_spent":320,"titan_id":"Titan70"},{"level":41,"quantity_received":428,"quantity_spent":411,"titan_id":"Titan59"},{"level":39,"quantity_received":373,"quantity_spent":368,"titan_id":"Titan54"},{"level":48,"quantity_received":898,"quantity_spent":886,"titan_id":"Titan9"},{"level":36,"quantity_received":128,"quantity_spent":127,"titan_id":"Titan91"},{"level":38,"quantity_received":146,"quantity_spent":142,"titan_id":"Titan80"},{"level":47,"quantity_received":855,"quantity_spent":839,"titan_id":"Titan24"},{"level":34,"quantity_received":116,"quantity_spent":113,"titan_id":"Titan99"},{"level":40,"quantity_received":384,"quantity_spent":379,"titan_id":"Titan66"},{"level":40,"quantity_received":405,"quantity_spent":389,"titan_id":"Titan36"},{"level":47,"quantity_received":863,"quantity_spent":839,"titan_id":"Titan29"},{"level":40,"quantity_received":402,"quantity_spent":389,"titan_id":"Titan58"},{"level":33,"quantity_received":80,"quantity_spent":80,"titan_id":"Titan111"},{"level":39,"quantity_received":373,"quantity_spent":368,"titan_id":"Titan38"},{"level":40,"quantity_received":379,"quantity_spent":379,"titan_id":"Titan79"},{"level":34,"quantity_received":86,"quantity_spent":85,"titan_id":"Titan101"},{"level":47,"quantity_received":876,"quantity_spent":839,"titan_id":"Titan5"},{"level":35,"quantity_received":123,"quantity_spent":120,"titan_id":"Titan84"},{"level":47,"quantity_received":879,"quantity_spent":839,"titan_id":"Titan26"},{"level":47,"quantity_received":885,"quantity_spent":839,"titan_id":"Titan11"},{"level":47,"quantity_received":867,"quantity_spent":839,"titan_id":"Titan4"},{"level":43,"quantity_received":461,"quantity_spent":458,"titan_id":"Titan30"},{"level":41,"quantity_received":419,"quantity_spent":411,"titan_id":"Titan55"},{"level":43,"quantity_received":469,"quantity_spent":458,"titan_id":"Titan46"},{"level":43,"quantity_received":453,"quantity_spent":445,"titan_id":"Titan60"},{"level":46,"quantity_received":828,"quantity_spent":795,"titan_id":"Titan23"},{"level":50,"quantity_received":1013,"quantity_spent":990,"titan_id":"Titan16"},{"level":40,"quantity_received":392,"quantity_spent":389,"titan_id":"Titan37"},{"level":41,"quantity_received":407,"quantity_spent":400,"titan_id":"Titan68"},{"level":39,"quantity_received":368,"quantity_spent":368,"titan_id":"Titan33"},{"level":47,"quantity_received":840,"quantity_spent":839,"titan_id":"Titan18"},{"level":47,"quantity_received":876,"quantity_spent":839,"titan_id":"Titan8"},{"level":39,"quantity_received":388,"quantity_spent":368,"titan_id":"Titan43"},{"level":47,"quantity_received":881,"quantity_spent":839,"titan_id":"Titan28"},{"level":48,"quantity_received":894,"quantity_spent":886,"titan_id":"Titan19"},{"level":38,"quantity_received":356,"quantity_spent":348,"titan_id":"Titan48"},{"level":47,"quantity_received":856,"quantity_spent":839,"titan_id":"Titan15"},{"level":47,"quantity_received":885,"quantity_spent":839,"titan_id":"Titan21"},{"level":47,"quantity_received":856,"quantity_spent":839,"titan_id":"Titan6"},{"level":47,"quantity_received":859,"quantity_spent":839,"titan_id":"Titan22"},{"level":47,"quantity_received":864,"quantity_spent":839,"titan_id":"Titan3"},{"level":38,"quantity_received":357,"quantity_spent":339,"titan_id":"Titan69"},{"level":47,"quantity_received":868,"quantity_spent":839,"titan_id":"Titan7"},{"level":46,"quantity_received":838,"quantity_spent":795,"titan_id":"Titan20"},{"level":43,"quantity_received":468,"quantity_spent":458,"titan_id":"Titan40"},{"level":49,"quantity_received":965,"quantity_spent":936,"titan_id":"Titan0"},{"level":39,"quantity_received":368,"quantity_spent":368,"titan_id":"Titan56"}],"titan_points":"56139","total_card_level":"1441","total_clan_scrolls":"6495","total_helper_weapons":"6731","total_pet_levels":"25130","total_raid_player_xp":"1383614","total_skill_points":"9003","total_tournaments":"406","undisputed_count":"72","weekly_ticket_count":"462"}'''

_clan_kick_optional_executor = '''{"clan_code": "test", "executor": {}, "player": {"name": "test", "player_code": "test"}}'''