from unittest import TestCase

from tap_titans.models import models
from tap_titans.abcs.rest_api import ClanDataResp


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
                    ('clan_code', (
                        '"clan_code":"test"',
                        '"clan_code": "test"',
                        '"clan_code": "string"',
                        '"clan_code":"string"',
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

_clan_data = '''{"clan_code": "test","clan_name": "test","players_data": [{"cards": [{"level": 40,"quantity_received": 3083,"quantity_spent": 2785,"skill_name": "AstralEcho"},{"level": 37,"quantity_received": 4030,"quantity_spent": 3839,"skill_name": "BurningAttack"},{"level": 42,"quantity_received": 4368,"quantity_spent": 4077,"skill_name": "BurstBoost"},{"level": 33,"quantity_received": 3398,"quantity_spent": 3201,"skill_name": "BurstCount"},{"level": 41,"quantity_received": 2948,"quantity_spent": 2809,"skill_name": "CelestialStatic"},{"level": 38,"quantity_received": 3860,"quantity_spent": 3813,"skill_name": "ChainLightning"},{"level": 33,"quantity_received": 3308,"quantity_spent": 3286,"skill_name": "CrushingVoid"},{"level": 28,"quantity_received": 3260,"quantity_spent": 2963,"skill_name": "DecayingAttack"},{"level": 34,"quantity_received": 3424,"quantity_spent": 3234,"skill_name": "Disease"},{"level": 35,"quantity_received": 3558,"quantity_spent": 3275,"skill_name": "ExecutionersAxe"},{"level": 30,"quantity_received": 2830,"quantity_spent": 2828,"skill_name": "FinisherAttack"},{"level": 29,"quantity_received": 3185,"quantity_spent": 3133,"skill_name": "FlakShot"},{"level": 30,"quantity_received": 3070,"quantity_spent": 2744,"skill_name": "Fragmentize"},{"level": 31,"quantity_received": 3675,"quantity_spent": 3590,"skill_name": "Fuse"},{"level": 33,"quantity_received": 3833,"quantity_spent": 3513,"skill_name": "Haymaker"},{"level": 32,"quantity_received": 3418,"quantity_spent": 3418,"skill_name": "ImpactAttack"},{"level": 30,"quantity_received": 3064,"quantity_spent": 2751,"skill_name": "InnerTruth"},{"level": 28,"quantity_received": 3285,"quantity_spent": 3223,"skill_name": "LimbBurst"},{"level": 32,"quantity_received": 3480,"quantity_spent": 3445,"skill_name": "LimbSupport"},{"level": 49,"quantity_received": 2236,"quantity_spent": 2165,"skill_name": "MagicPotion"},{"level": 38,"quantity_received": 3937,"quantity_spent": 3642,"skill_name": "MentalFocus"},{"level": 45,"quantity_received": 4362,"quantity_spent": 4103,"skill_name": "MirrorForce"},{"level": 32,"quantity_received": 3516,"quantity_spent": 3499,"skill_name": "MoonBeam"},{"level": 34,"quantity_received": 3697,"quantity_spent": 3675,"skill_name": "PlagueAttack"},{"level": 25,"quantity_received": 2851,"quantity_spent": 2788,"skill_name": "PoisonAttack"},{"level": 32,"quantity_received": 2483,"quantity_spent": 2426,"skill_name": "PowerBubble"},{"level": 51,"quantity_received": 6141,"quantity_spent": 5749,"skill_name": "Purify"},{"level": 33,"quantity_received": 3781,"quantity_spent": 3691,"skill_name": "RazorWind"},{"level": 42,"quantity_received": 4847,"quantity_spent": 4655,"skill_name": "RuinousRust"},{"level": 31,"quantity_received": 2767,"quantity_spent": 2549,"skill_name": "RuneAttack"},{"level": 10,"quantity_received": 46,"quantity_spent": 14,"skill_name": "SandsOfTime"},{"level": 36,"quantity_received": 3692,"quantity_spent": 3416,"skill_name": "Shadow"},{"level": 28,"quantity_received": 3176,"quantity_spent": 3084,"skill_name": "SkullBash"},{"level": 37,"quantity_received": 3831,"quantity_spent": 3786,"skill_name": "SpinalTap"},{"level": 33,"quantity_received": 3593,"quantity_spent": 3374,"skill_name": "SuperheatMetal"},{"level": 30,"quantity_received": 2975,"quantity_spent": 2754,"skill_name": "Swarm"},{"level": 36,"quantity_received": 4052,"quantity_spent": 3721,"skill_name": "TeamTactics"},{"level": 50,"quantity_received": 6060,"quantity_spent": 5791,"skill_name": "TotemFairySkill"},{"level": 32,"quantity_received": 1214,"quantity_spent": 934,"skill_name": "TriangleSupport"},{"level": 28,"quantity_received": 72,"quantity_spent": 72,"skill_name": "Weaken"},{"level": 30,"quantity_received": 2944,"quantity_spent": 2831,"skill_name": "WhipOfLightning"}],"country_code": "UX","current_card_currency": 0,"daily_raid_tickets": 59217,"loyalty_level": 12,"max_stage": 365192,"name": "[TTU] Silical","player_code": "test","player_raid_level": 966,"previous_rank": "0.3829","raid_research_tree": {"ArmorDamage": 0.125,"ChestDamage": 0.1,"HeadDamage": 0.1,"LimbDamage": 0.1},"raid_wildcard_count": 3,"role": "CoLeader","summon_level": 218,"total_card_level": "1398","total_raid_player_xp": 1331387,"weekly_ticket_count": 198}]}'''

_player_data = '''{"additive_relic_multiplier":34957,"artifacts":[{"artifact_id":"Artifact1","is_enchanted":true,"level":"9.00000000000000E+98"},{"artifact_id":"Artifact10","is_enchanted":true,"level":"7.00000000000000E+103"},{"artifact_id":"Artifact100","is_enchanted":true,"level":"6.00000000000000E+103"},{"artifact_id":"Artifact101","is_enchanted":true,"level":"7.98000000000000E+103"},{"artifact_id":"Artifact102","is_enchanted":true,"level":"3.00000000000000E+91"},{"artifact_id":"Artifact103","is_enchanted":true,"level":"1.30000000000000E+84"},{"artifact_id":"Artifact11","is_enchanted":true,"level":"3.00000000000000E+91"},{"artifact_id":"Artifact12","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact13","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact14","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact15","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact16","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact17","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact18","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact19","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact2","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact20","is_enchanted":true,"level":"7.00000000000000E+87"},{"artifact_id":"Artifact21","is_enchanted":false,"level":"50"},{"artifact_id":"Artifact22","is_enchanted":true,"level":"3.56793200000000E+80"},{"artifact_id":"Artifact23","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact24","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact25","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact26","is_enchanted":true,"level":"7.00000000000000E+87"},{"artifact_id":"Artifact27","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact28","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact29","is_enchanted":true,"level":"1.20000000000000E+104"},{"artifact_id":"Artifact3","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact30","is_enchanted":true,"level":"1.10000000000000E+104"},{"artifact_id":"Artifact31","is_enchanted":true,"level":"4.00000000000000E+93"},{"artifact_id":"Artifact32","is_enchanted":true,"level":"1.10000000000000E+104"},{"artifact_id":"Artifact33","is_enchanted":true,"level":"1.10000000000000E+104"},{"artifact_id":"Artifact34","is_enchanted":true,"level":"1.00000000000000E+104"},{"artifact_id":"Artifact35","is_enchanted":true,"level":"1.10000000000000E+104"},{"artifact_id":"Artifact36","is_enchanted":false,"level":"20"},{"artifact_id":"Artifact37","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact38","is_enchanted":true,"level":"4.00000000000000E+93"},{"artifact_id":"Artifact39","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact4","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact40","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact41","is_enchanted":true,"level":"7.00000000000000E+103"},{"artifact_id":"Artifact42","is_enchanted":true,"level":"9.00000000000000E+103"},{"artifact_id":"Artifact43","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact44","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact45","is_enchanted":true,"level":"1.00000000000000E+88"},{"artifact_id":"Artifact46","is_enchanted":true,"level":"9.00000000000000E+103"},{"artifact_id":"Artifact47","is_enchanted":true,"level":"1.50000000000000E+100"},{"artifact_id":"Artifact48","is_enchanted":false,"level":"30"},{"artifact_id":"Artifact49","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact5","is_enchanted":false,"level":"50"},{"artifact_id":"Artifact50","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact51","is_enchanted":true,"level":"2.00000000000000E+93"},{"artifact_id":"Artifact52","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact53","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact54","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact55","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact56","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact57","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact58","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact59","is_enchanted":true,"level":"1.20000000000000E+104"},{"artifact_id":"Artifact6","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact60","is_enchanted":false,"level":"60"},{"artifact_id":"Artifact61","is_enchanted":true,"level":"1.00000000000000E+104"},{"artifact_id":"Artifact62","is_enchanted":true,"level":"1.00000000000000E+104"},{"artifact_id":"Artifact63","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact64","is_enchanted":true,"level":"1.00000000000000E+100"},{"artifact_id":"Artifact65","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact66","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact67","is_enchanted":true,"level":"1.00000000000000E+104"},{"artifact_id":"Artifact68","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact69","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact7","is_enchanted":true,"level":"7.00000000000000E+103"},{"artifact_id":"Artifact70","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"Artifact71","is_enchanted":false,"level":"50.0000000000000"},{"artifact_id":"Artifact72","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"Artifact73","is_enchanted":true,"level":"3.00000000000000E+93"},{"artifact_id":"Artifact74","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"Artifact75","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact76","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact77","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact78","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact79","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact8","is_enchanted":false,"level":"40"},{"artifact_id":"Artifact80","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"Artifact81","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"Artifact82","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact83","is_enchanted":true,"level":"4.00000000000000E+93"},{"artifact_id":"Artifact84","is_enchanted":true,"level":"7.00000000000000E+87"},{"artifact_id":"Artifact85","is_enchanted":false,"level":"50.0000000000000"},{"artifact_id":"Artifact86","is_enchanted":true,"level":"4.00000000000000E+87"},{"artifact_id":"Artifact87","is_enchanted":true,"level":"4.00000000000000E+87"},{"artifact_id":"Artifact88","is_enchanted":true,"level":"4.00000000000000E+87"},{"artifact_id":"Artifact89","is_enchanted":true,"level":"4.00000000000000E+87"},{"artifact_id":"Artifact9","is_enchanted":true,"level":"7.00000000000000E+103"},{"artifact_id":"Artifact90","is_enchanted":true,"level":"4.00000000000000E+87"},{"artifact_id":"Artifact91","is_enchanted":false,"level":"50.0000000000000"},{"artifact_id":"Artifact92","is_enchanted":false,"level":"50.0000000000000"},{"artifact_id":"Artifact93","is_enchanted":false,"level":"50.0000000000000"},{"artifact_id":"Artifact94","is_enchanted":true,"level":"7.00000000000000E+87"},{"artifact_id":"Artifact95","is_enchanted":true,"level":"2.00000000000000E+100"},{"artifact_id":"Artifact96","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact97","is_enchanted":true,"level":"5.00000000000000E+87"},{"artifact_id":"Artifact98","is_enchanted":true,"level":"3.00000000000000E+91"},{"artifact_id":"Artifact99","is_enchanted":true,"level":"3.00000000000000E+91"}],"badge_count":{"0":0,"1":0,"2":19,"3":13,"4":1},"cards":[{"level":40,"quantity_received":3083,"quantity_spent":2785,"skill_name":"AstralEcho"},{"level":37,"quantity_received":4030,"quantity_spent":3839,"skill_name":"BurningAttack"},{"level":42,"quantity_received":4368,"quantity_spent":4077,"skill_name":"BurstBoost"},{"level":33,"quantity_received":3398,"quantity_spent":3201,"skill_name":"BurstCount"},{"level":41,"quantity_received":2948,"quantity_spent":2809,"skill_name":"CelestialStatic"},{"level":38,"quantity_received":3860,"quantity_spent":3813,"skill_name":"ChainLightning"},{"level":33,"quantity_received":3308,"quantity_spent":3286,"skill_name":"CrushingVoid"},{"level":28,"quantity_received":3260,"quantity_spent":2963,"skill_name":"DecayingAttack"},{"level":34,"quantity_received":3424,"quantity_spent":3234,"skill_name":"Disease"},{"level":35,"quantity_received":3558,"quantity_spent":3275,"skill_name":"ExecutionersAxe"},{"level":30,"quantity_received":2830,"quantity_spent":2828,"skill_name":"FinisherAttack"},{"level":29,"quantity_received":3185,"quantity_spent":3133,"skill_name":"FlakShot"},{"level":30,"quantity_received":3070,"quantity_spent":2744,"skill_name":"Fragmentize"},{"level":31,"quantity_received":3675,"quantity_spent":3590,"skill_name":"Fuse"},{"level":33,"quantity_received":3833,"quantity_spent":3513,"skill_name":"Haymaker"},{"level":32,"quantity_received":3418,"quantity_spent":3418,"skill_name":"ImpactAttack"},{"level":30,"quantity_received":3064,"quantity_spent":2751,"skill_name":"InnerTruth"},{"level":28,"quantity_received":3285,"quantity_spent":3223,"skill_name":"LimbBurst"},{"level":32,"quantity_received":3480,"quantity_spent":3445,"skill_name":"LimbSupport"},{"level":49,"quantity_received":2236,"quantity_spent":2165,"skill_name":"MagicPotion"},{"level":38,"quantity_received":3937,"quantity_spent":3642,"skill_name":"MentalFocus"},{"level":45,"quantity_received":4362,"quantity_spent":4103,"skill_name":"MirrorForce"},{"level":32,"quantity_received":3516,"quantity_spent":3499,"skill_name":"MoonBeam"},{"level":34,"quantity_received":3697,"quantity_spent":3675,"skill_name":"PlagueAttack"},{"level":25,"quantity_received":2851,"quantity_spent":2788,"skill_name":"PoisonAttack"},{"level":32,"quantity_received":2483,"quantity_spent":2426,"skill_name":"PowerBubble"},{"level":51,"quantity_received":6141,"quantity_spent":5749,"skill_name":"Purify"},{"level":33,"quantity_received":3781,"quantity_spent":3691,"skill_name":"RazorWind"},{"level":42,"quantity_received":4847,"quantity_spent":4655,"skill_name":"RuinousRust"},{"level":31,"quantity_received":2767,"quantity_spent":2549,"skill_name":"RuneAttack"},{"level":10,"quantity_received":46,"quantity_spent":14,"skill_name":"SandsOfTime"},{"level":36,"quantity_received":3692,"quantity_spent":3416,"skill_name":"Shadow"},{"level":28,"quantity_received":3176,"quantity_spent":3084,"skill_name":"SkullBash"},{"level":37,"quantity_received":3831,"quantity_spent":3786,"skill_name":"SpinalTap"},{"level":33,"quantity_received":3593,"quantity_spent":3374,"skill_name":"SuperheatMetal"},{"level":30,"quantity_received":2975,"quantity_spent":2754,"skill_name":"Swarm"},{"level":36,"quantity_received":4052,"quantity_spent":3721,"skill_name":"TeamTactics"},{"level":50,"quantity_received":6060,"quantity_spent":5791,"skill_name":"TotemFairySkill"},{"level":32,"quantity_received":1214,"quantity_spent":934,"skill_name":"TriangleSupport"},{"level":28,"quantity_received":72,"quantity_spent":72,"skill_name":"Weaken"},{"level":30,"quantity_received":2944,"quantity_spent":2831,"skill_name":"WhipOfLightning"}],"challenge_tournaments_participation":"124","challenge_tournaments_undisputed_count":"1","clan_code":"test","clan_name":"TT Universe","clan_scroll":[{"Level":344,"ScrollId":"ScrollId11"},{"Level":345,"ScrollId":"ScrollId17"},{"Level":342,"ScrollId":"ScrollId12"},{"Level":344,"ScrollId":"ScrollId3"},{"Level":344,"ScrollId":"ScrollId4"},{"Level":344,"ScrollId":"ScrollId15"},{"Level":345,"ScrollId":"ScrollId7"},{"Level":343,"ScrollId":"ScrollId6"},{"Level":342,"ScrollId":"ScrollId18"},{"Level":343,"ScrollId":"ScrollId10"},{"Level":343,"ScrollId":"ScrollId5"},{"Level":342,"ScrollId":"ScrollId16"},{"Level":344,"ScrollId":"ScrollId2"},{"Level":344,"ScrollId":"ScrollId9"},{"Level":342,"ScrollId":"ScrollId14"},{"Level":342,"ScrollId":"ScrollId8"},{"Level":347,"ScrollId":"ScrollId13"},{"Level":343,"ScrollId":"ScrollId1"}],"country_code":"UX","crafting_shards_spent":19320,"current_card_currency":0,"current_world_id":"54","daily_raid_tickets":"59217","equipment_set":["Devil","Green","SteelHero","SpellBooster","FairyKnight","Headless","Crow","SnakeOil","AnniversaryFairy","TwilightFairyKing","BlueKnight","RockGirl","Captain","AlphaHeart","Diamond","BlueFlame","WaterSorcerer","Grill","Stone","Dancer","PetChampion","Meat","Slayer","Quinn","Tropical","GoldenMech","Spellmaster","MetallicLightning","Rosabella","Scout","Grinch","DaggerRogue","Damon","Greed","Blacksmith","PetTamer","Lance","Picnic","Scarecrow","RaidCaptain","HighTecLightning","Titania","Beach","Scientist","Frost","BunnyDroid","Pyro","Doll","Snowboard","Punk","SunBather","DarkAngel","Titan","Vampire","GoldAngel","Enchant","SoulCatcher","FirstMate","Gulbrand","Jade","Gingerbread","Chakram","Ninja","ScrollMaster","Medic","Ninetails","Cowboy","Thief","SpaceKnight","Demon","Cyborg","Maple","Shepherd","EarthRogue","Sun","Hollow","Cupid","Lifeguard","Jayce","ElderSnow","ElectricWarlord","CNY","Monk","WarHorn","Padlock","Rockstar","Spacesuit","Mage","AirshipEngineer","Pharaoh","PerkMaster","Skulls","Gambler","LightBunny","Knight","Gamer","FireKnight","Anniversary","Corrupted","Rogue","Baker","Aquamarine","Pirate","ShadowMagician","Dungeoneer","Bard","Yeti","Lolita","DOS","Ghost","Bane","FairyShaman","Ninjitsu","Hunter","Jukk","SoloRaid","PlagueDoctor","LifetimePrestige","Twilight","SteampunkKnight","ManaMage","Snowman","Kronus","Reaper","Surf","Dragon","Viking","Wonder","Platinum","Fur","Spartan","Sports","RaidMythic","Zeus","Witch","Runestone","Samurai","Prestigious","Tank","FireTribe","FireCook","MultiCast","Nomad","GoldGun","BoneTribe","Wolf","Sophia","WeaponMaster","Jester","Bishop","Bazooka","Midas","Chains","Gundam","Musketeer","Influencer","Sled","TimeWizard","Poet","Mech","DarkAlien","WildCat","GoldRain","BlackDragon"],"equipment_set_count":"164","hero_weapon":[{"HelperID":"H16","Level":177},{"HelperID":"H23","Level":173},{"HelperID":"H37","Level":178},{"HelperID":"H09","Level":174},{"HelperID":"H25","Level":173},{"HelperID":"H04","Level":173},{"HelperID":"H27","Level":174},{"HelperID":"H18","Level":178},{"HelperID":"H03","Level":173},{"HelperID":"H29","Level":174},{"HelperID":"H06","Level":174},{"HelperID":"H21","Level":177},{"HelperID":"H05","Level":174},{"HelperID":"H07","Level":174},{"HelperID":"H30","Level":173},{"HelperID":"H33","Level":173},{"HelperID":"H26","Level":174},{"HelperID":"H02","Level":175},{"HelperID":"H11","Level":178},{"HelperID":"H01","Level":173},{"HelperID":"H15","Level":177},{"HelperID":"H10","Level":177},{"HelperID":"H14","Level":174},{"HelperID":"H20","Level":173},{"HelperID":"H24","Level":173},{"HelperID":"H32","Level":175},{"HelperID":"H08","Level":173},{"HelperID":"H12","Level":174},{"HelperID":"H31","Level":176},{"HelperID":"H36","Level":175},{"HelperID":"H22","Level":173},{"HelperID":"H34","Level":173},{"HelperID":"H19","Level":173},{"HelperID":"H17","Level":173},{"HelperID":"H13","Level":173},{"HelperID":"H28","Level":175},{"HelperID":"H35","Level":173}],"loyalty_level":"12","max_stage":365192,"name":"[TTU] Silical","pets":[{"level":1143,"pet_id":"Pet1"},{"level":906,"pet_id":"Pet10"},{"level":859,"pet_id":"Pet11"},{"level":867,"pet_id":"Pet12"},{"level":927,"pet_id":"Pet13"},{"level":965,"pet_id":"Pet14"},{"level":1156,"pet_id":"Pet15"},{"level":895,"pet_id":"Pet16"},{"level":579,"pet_id":"Pet17"},{"level":611,"pet_id":"Pet18"},{"level":596,"pet_id":"Pet19"},{"level":990,"pet_id":"Pet2"},{"level":616,"pet_id":"Pet20"},{"level":703,"pet_id":"Pet21"},{"level":664,"pet_id":"Pet22"},{"level":626,"pet_id":"Pet23"},{"level":646,"pet_id":"Pet24"},{"level":639,"pet_id":"Pet25"},{"level":671,"pet_id":"Pet26"},{"level":626,"pet_id":"Pet27"},{"level":612,"pet_id":"Pet28"},{"level":595,"pet_id":"Pet29"},{"level":889,"pet_id":"Pet3"},{"level":728,"pet_id":"Pet30"},{"level":873,"pet_id":"Pet4"},{"level":887,"pet_id":"Pet5"},{"level":911,"pet_id":"Pet6"},{"level":1018,"pet_id":"Pet7"},{"level":999,"pet_id":"Pet8"},{"level":856,"pet_id":"Pet9"},{"level":164,"pet_id":"SeasonalPet1"},{"level":171,"pet_id":"SeasonalPet10"},{"level":165,"pet_id":"SeasonalPet12"},{"level":166,"pet_id":"SeasonalPet15"},{"level":180,"pet_id":"SeasonalPet2"},{"level":172,"pet_id":"SeasonalPet3"},{"level":173,"pet_id":"SeasonalPet4"},{"level":168,"pet_id":"SeasonalPet7"},{"level":180,"pet_id":"SeasonalPet8"},{"level":182,"pet_id":"SeasonalPet9"}],"player_code":"test","player_raid_level":"966","previous_rank":"0.3829","raid_research_tree":{"ArmorDamage":0.125,"ChestDamage":0.1,"HeadDamage":0.1,"LimbDamage":0.1},"raid_wildcard_count":3,"relics_received":"1.69832546567531E+282","relics_spent":"8.94261436670921E+281","role":"CoLeader","seasonal_artifacts":[{"artifact_id":"SeasonalArtifact1","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"SeasonalArtifact10","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact15","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact19","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact2","is_enchanted":false,"level":"18011.0000000000"},{"artifact_id":"SeasonalArtifact20","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact21","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact22","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"SeasonalArtifact3","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact34","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact35","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact36","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"SeasonalArtifact37","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact38","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact39","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact4","is_enchanted":false,"level":"20696.0000000000"},{"artifact_id":"SeasonalArtifact40","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact42","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact43","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact5","is_enchanted":false,"level":"19578.0000000000"},{"artifact_id":"SeasonalArtifact6","is_enchanted":false,"level":"18000.0000000000"},{"artifact_id":"SeasonalArtifact7","is_enchanted":false,"level":"40.0000000000000"},{"artifact_id":"SeasonalArtifact9","is_enchanted":false,"level":"40.0000000000000"}],"seasonal_relic_multiplier":1055,"seasonal_relics_received":"763658517681048000000000000000000","seasonal_relics_spent":"602870028861049000000000000000000","skill_tree":[{"level":4,"skill_id":"TapDmg"},{"level":4,"skill_id":"TapDmgFromHelpers"},{"level":1,"skill_id":"BurstSkillBoost"},{"level":1,"skill_id":"FairyGold"},{"level":17,"skill_id":"HeavyStrikes"},{"level":9,"skill_id":"FairyChance"},{"level":2,"skill_id":"PetDmg"},{"level":5,"skill_id":"PetGoldQTE"},{"level":24,"skill_id":"PetEquipmentBoost"},{"level":30,"skill_id":"CombatTechniques"},{"level":9,"skill_id":"AllHelperDmg"},{"level":23,"skill_id":"HelperBoost"},{"level":12,"skill_id":"HelperDmgSkillBoost"},{"level":30,"skill_id":"ClanShipDmg"},{"level":13,"skill_id":"ClanQTE"},{"level":16,"skill_id":"HelperInspiredWeaken"},{"level":30,"skill_id":"ClanShipStun"},{"level":13,"skill_id":"HelperDmgQTE"},{"level":3,"skill_id":"HelperBoostMultiCastSkill"},{"level":18,"skill_id":"ClanShipVoltage"},{"level":3,"skill_id":"ClanShipVoltageMultiCastSkill"},{"level":2,"skill_id":"CloneDmg"},{"level":5,"skill_id":"MPCapacityBoost"},{"level":1,"skill_id":"CloneSkillBoost"},{"level":1,"skill_id":"ManaStealSkillBoost"},{"level":1,"skill_id":"ManaMonster"},{"level":19,"skill_id":"BossTimer"},{"level":8,"skill_id":"CritSkillBoost"},{"level":19,"skill_id":"ForbiddenContract"},{"level":20,"skill_id":"TerrifyingPact"},{"level":2,"skill_id":"OfflineGold"},{"level":4,"skill_id":"CritSkillBoostDmg"},{"level":1,"skill_id":"UltraDagger"},{"level":9,"skill_id":"Cloaking"},{"level":14,"skill_id":"Backstab"},{"level":29,"skill_id":"PoisonedBlade"},{"level":4,"skill_id":"MultiMonsters"},{"level":2,"skill_id":"GuidedBlade"},{"level":10,"skill_id":"LoadedDice"},{"level":4,"skill_id":"Transmutation"},{"level":6,"skill_id":"ChestGold"},{"level":6,"skill_id":"MidasSkillBoost"},{"level":9,"skill_id":"LovePotion"},{"level":2,"skill_id":"HandOfMidasMultiCastSkillBoost"},{"level":20,"skill_id":"KratosSummon"},{"level":13,"skill_id":"RoyalContract"}],"summon_level":218,"titan_cards":[{"level":31,"quantity_received":227,"quantity_spent":226,"titan_id":"Titan35"},{"level":29,"quantity_received":85,"quantity_spent":82,"titan_id":"Titan85"},{"level":25,"quantity_received":65,"quantity_spent":62,"titan_id":"Titan99"},{"level":19,"quantity_received":31,"quantity_spent":29,"titan_id":"Titan111"},{"level":26,"quantity_received":52,"quantity_spent":51,"titan_id":"Titan119"},{"level":28,"quantity_received":80,"quantity_spent":77,"titan_id":"Titan84"},{"level":26,"quantity_received":70,"quantity_spent":67,"titan_id":"Titan87"},{"level":29,"quantity_received":84,"quantity_spent":82,"titan_id":"Titan81"},{"level":27,"quantity_received":76,"quantity_spent":72,"titan_id":"Titan83"},{"level":26,"quantity_received":70,"quantity_spent":67,"titan_id":"Titan88"},{"level":27,"quantity_received":75,"quantity_spent":72,"titan_id":"Titan90"},{"level":29,"quantity_received":85,"quantity_spent":82,"titan_id":"Titan89"},{"level":23,"quantity_received":43,"quantity_spent":41,"titan_id":"Titan104"},{"level":26,"quantity_received":53,"quantity_spent":51,"titan_id":"Titan113"},{"level":27,"quantity_received":76,"quantity_spent":72,"titan_id":"Titan82"},{"level":26,"quantity_received":51,"quantity_spent":51,"titan_id":"Titan110"},{"level":25,"quantity_received":48,"quantity_spent":47,"titan_id":"Titan101"},{"level":26,"quantity_received":54,"quantity_spent":51,"titan_id":"Titan102"},{"level":22,"quantity_received":40,"quantity_spent":38,"titan_id":"Titan112"},{"level":23,"quantity_received":43,"quantity_spent":41,"titan_id":"Titan106"},{"level":26,"quantity_received":67,"quantity_spent":67,"titan_id":"Titan97"},{"level":22,"quantity_received":38,"quantity_spent":38,"titan_id":"Titan114"},{"level":21,"quantity_received":37,"quantity_spent":35,"titan_id":"Titan115"},{"level":23,"quantity_received":43,"quantity_spent":41,"titan_id":"Titan105"},{"level":29,"quantity_received":86,"quantity_spent":82,"titan_id":"Titan95"},{"level":24,"quantity_received":44,"quantity_spent":44,"titan_id":"Titan103"},{"level":22,"quantity_received":39,"quantity_spent":38,"titan_id":"Titan107"},{"level":23,"quantity_received":42,"quantity_spent":41,"titan_id":"Titan109"},{"level":26,"quantity_received":52,"quantity_spent":51,"titan_id":"Titan108"},{"level":28,"quantity_received":81,"quantity_spent":77,"titan_id":"Titan80"},{"level":24,"quantity_received":44,"quantity_spent":44,"titan_id":"Titan116"},{"level":31,"quantity_received":226,"quantity_spent":221,"titan_id":"Titan70"},{"level":31,"quantity_received":96,"quantity_spent":94,"titan_id":"Titan93"},{"level":36,"quantity_received":305,"quantity_spent":302,"titan_id":"Titan60"},{"level":34,"quantity_received":289,"quantity_spent":274,"titan_id":"Titan50"},{"level":32,"quantity_received":244,"quantity_spent":236,"titan_id":"Titan71"},{"level":35,"quantity_received":302,"quantity_spent":291,"titan_id":"Titan30"},{"level":43,"quantity_received":687,"quantity_spent":678,"titan_id":"Titan8"},{"level":34,"quantity_received":273,"quantity_spent":268,"titan_id":"Titan76"},{"level":28,"quantity_received":81,"quantity_spent":77,"titan_id":"Titan96"},{"level":34,"quantity_received":290,"quantity_spent":274,"titan_id":"Titan55"},{"level":33,"quantity_received":260,"quantity_spent":257,"titan_id":"Titan36"},{"level":31,"quantity_received":224,"quantity_spent":221,"titan_id":"Titan73"},{"level":33,"quantity_received":259,"quantity_spent":257,"titan_id":"Titan45"},{"level":28,"quantity_received":61,"quantity_spent":59,"titan_id":"Titan100"},{"level":27,"quantity_received":72,"quantity_spent":72,"titan_id":"Titan91"},{"level":32,"quantity_received":253,"quantity_spent":241,"titan_id":"Titan34"},{"level":44,"quantity_received":743,"quantity_spent":715,"titan_id":"Titan0"},{"level":34,"quantity_received":282,"quantity_spent":274,"titan_id":"Titan59"},{"level":35,"quantity_received":298,"quantity_spent":291,"titan_id":"Titan40"},{"level":43,"quantity_received":690,"quantity_spent":678,"titan_id":"Titan26"},{"level":42,"quantity_received":671,"quantity_spent":642,"titan_id":"Titan6"},{"level":25,"quantity_received":48,"quantity_spent":47,"titan_id":"Titan118"},{"level":43,"quantity_received":682,"quantity_spent":678,"titan_id":"Titan5"},{"level":42,"quantity_received":661,"quantity_spent":642,"titan_id":"Titan24"},{"level":32,"quantity_received":239,"quantity_spent":236,"titan_id":"Titan75"},{"level":32,"quantity_received":249,"quantity_spent":236,"titan_id":"Titan66"},{"level":42,"quantity_received":677,"quantity_spent":642,"titan_id":"Titan14"},{"level":32,"quantity_received":250,"quantity_spent":241,"titan_id":"Titan56"},{"level":45,"quantity_received":791,"quantity_spent":754,"titan_id":"Titan16"},{"level":32,"quantity_received":242,"quantity_spent":236,"titan_id":"Titan61"},{"level":27,"quantity_received":76,"quantity_spent":72,"titan_id":"Titan92"},{"level":32,"quantity_received":242,"quantity_spent":236,"titan_id":"Titan67"},{"level":32,"quantity_received":250,"quantity_spent":241,"titan_id":"Titan38"},{"level":33,"quantity_received":257,"quantity_spent":252,"titan_id":"Titan63"},{"level":34,"quantity_received":279,"quantity_spent":268,"titan_id":"Titan77"},{"level":32,"quantity_received":255,"quantity_spent":241,"titan_id":"Titan39"},{"level":24,"quantity_received":46,"quantity_spent":44,"titan_id":"Titan117"},{"level":42,"quantity_received":671,"quantity_spent":642,"titan_id":"Titan27"},{"level":45,"quantity_received":760,"quantity_spent":754,"titan_id":"Titan10"},{"level":33,"quantity_received":262,"quantity_spent":257,"titan_id":"Titan43"},{"level":42,"quantity_received":654,"quantity_spent":642,"titan_id":"Titan12"},{"level":33,"quantity_received":264,"quantity_spent":257,"titan_id":"Titan58"},{"level":31,"quantity_received":221,"quantity_spent":221,"titan_id":"Titan62"},{"level":31,"quantity_received":228,"quantity_spent":221,"titan_id":"Titan65"},{"level":32,"quantity_received":246,"quantity_spent":241,"titan_id":"Titan33"},{"level":42,"quantity_received":677,"quantity_spent":642,"titan_id":"Titan7"},{"level":42,"quantity_received":669,"quantity_spent":642,"titan_id":"Titan21"},{"level":31,"quantity_received":230,"quantity_spent":221,"titan_id":"Titan69"},{"level":32,"quantity_received":249,"quantity_spent":241,"titan_id":"Titan32"},{"level":27,"quantity_received":76,"quantity_spent":72,"titan_id":"Titan98"},{"level":33,"quantity_received":258,"quantity_spent":257,"titan_id":"Titan53"},{"level":35,"quantity_received":294,"quantity_spent":291,"titan_id":"Titan57"},{"level":31,"quantity_received":228,"quantity_spent":221,"titan_id":"Titan64"},{"level":42,"quantity_received":645,"quantity_spent":642,"titan_id":"Titan3"},{"level":43,"quantity_received":708,"quantity_spent":678,"titan_id":"Titan19"},{"level":42,"quantity_received":660,"quantity_spent":642,"titan_id":"Titan15"},{"level":33,"quantity_received":261,"quantity_spent":252,"titan_id":"Titan74"},{"level":33,"quantity_received":262,"quantity_spent":252,"titan_id":"Titan72"},{"level":33,"quantity_received":269,"quantity_spent":257,"titan_id":"Titan47"},{"level":33,"quantity_received":267,"quantity_spent":257,"titan_id":"Titan44"},{"level":42,"quantity_received":643,"quantity_spent":642,"titan_id":"Titan22"},{"level":42,"quantity_received":651,"quantity_spent":642,"titan_id":"Titan2"},{"level":42,"quantity_received":665,"quantity_spent":642,"titan_id":"Titan17"},{"level":35,"quantity_received":302,"quantity_spent":291,"titan_id":"Titan46"},{"level":41,"quantity_received":626,"quantity_spent":608,"titan_id":"Titan23"},{"level":44,"quantity_received":719,"quantity_spent":715,"titan_id":"Titan9"},{"level":33,"quantity_received":264,"quantity_spent":252,"titan_id":"Titan68"},{"level":33,"quantity_received":264,"quantity_spent":257,"titan_id":"Titan49"},{"level":32,"quantity_received":251,"quantity_spent":241,"titan_id":"Titan54"},{"level":42,"quantity_received":646,"quantity_spent":642,"titan_id":"Titan20"},{"level":42,"quantity_received":642,"quantity_spent":642,"titan_id":"Titan18"},{"level":32,"quantity_received":253,"quantity_spent":241,"titan_id":"Titan51"},{"level":42,"quantity_received":664,"quantity_spent":642,"titan_id":"Titan4"},{"level":43,"quantity_received":690,"quantity_spent":678,"titan_id":"Titan13"},{"level":43,"quantity_received":689,"quantity_spent":678,"titan_id":"Titan28"},{"level":42,"quantity_received":668,"quantity_spent":642,"titan_id":"Titan29"},{"level":33,"quantity_received":258,"quantity_spent":257,"titan_id":"Titan41"},{"level":32,"quantity_received":246,"quantity_spent":241,"titan_id":"Titan48"},{"level":32,"quantity_received":253,"quantity_spent":241,"titan_id":"Titan52"},{"level":32,"quantity_received":238,"quantity_spent":236,"titan_id":"Titan79"},{"level":41,"quantity_received":636,"quantity_spent":608,"titan_id":"Titan25"},{"level":34,"quantity_received":272,"quantity_spent":268,"titan_id":"Titan78"},{"level":33,"quantity_received":258,"quantity_spent":257,"titan_id":"Titan37"},{"level":28,"quantity_received":79,"quantity_spent":77,"titan_id":"Titan86"},{"level":33,"quantity_received":109,"quantity_spent":106,"titan_id":"Titan94"},{"level":41,"quantity_received":629,"quantity_spent":608,"titan_id":"Titan1"},{"level":32,"quantity_received":248,"quantity_spent":241,"titan_id":"Titan31"},{"level":42,"quantity_received":659,"quantity_spent":642,"titan_id":"Titan11"},{"level":34,"quantity_received":278,"quantity_spent":274,"titan_id":"Titan42"}],"titan_points":"54039","total_card_level":"1398","total_clan_scrolls":"6183","total_helper_weapons":"6452","total_pet_levels":"24053","total_raid_player_xp":"1331387","total_skill_points":"8783","total_tournaments":"393","undisputed_count":"70","weekly_ticket_count":"198"}'''

_clan_kick_optional_executor = '''{"clan_code": "test", "executor": {}, "player": {"name": "test", "player_code": "test"}}'''