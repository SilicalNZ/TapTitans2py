from pydantic.fields import Field

from tap_titans.models import model_type
from tap_titans.utils.base import BaseModel



class ExportPlayerStats(BaseModel):
    input_max_prestige_state: str = Field(alias="Max Prestige Stage")
    input_artifacts_collected: str = Field(alias="Artifacts Collected")
    input_crafting_power: str = Field(alias="Crafting Power")
    input_total_pet_levels: str = Field(alias="Total Pet Levels")
    input_skill_points_owned: str = Field(alias="Skill Points Owned")
    input_hero_weapon_upgrades: str = Field(alias="Hero Weapon Upgrades")
    input_hero_scroll_upgrades: str = Field(alias="Hero Scroll Upgrades")
    input_tournaments_joined: str = Field(alias="Tournaments Joined")
    input_undisputed_wins: str = Field(alias="Undisputed Wins")
    input_tournament_points: str = Field(alias="Tournament Points")
    input_lifetime_relics: str = Field(alias="Lifetime Relics")

    @property
    def max_prestige_state(self) -> int:
        return int(self.input_max_prestige_state)

    @property
    def artifacts_collected(self) -> int:
        return int(self.input_artifacts_collected)

    @property
    def crafting_power(self) -> int:
        return int(self.input_crafting_power)

    @property
    def total_pet_levels(self) -> int:
        return int(self.input_total_pet_levels)

    @property
    def skill_points_owned(self) -> int:
        return int(self.input_skill_points_owned)

    @property
    def hero_weapon_upgrades(self) -> int:
        return int(self.input_hero_weapon_upgrades)

    @property
    def hero_scroll_upgrades(self) -> int:
        return int(self.input_hero_scroll_upgrades)

    @property
    def tournaments_joined(self) -> int:
        return int(self.input_tournaments_joined)

    @property
    def undisputed_wins(self) -> int:
        return int(self.input_undisputed_wins)

    @property
    def tournament_points(self) -> int:
        return int(self.input_tournament_points)

    @property
    def lifetime_relics(self) -> float:
        return float(self.input_lifetime_relics)


class ExportRaidStats(BaseModel):
    input_raid_level: str = Field(alias="Raid Level")
    input_raid_damage: str = Field(alias="Raid Damage")
    input_total_raid_experience: str = Field(alias="Total Raid Experience")
    input_total_raid_attacks: str = Field(alias="Total Raid Attacks")
    input_total_raid_card_levels: str = Field(alias="Total Raid Card Levels")
    input_raid_cards_owned: str = Field(alias="Raid Cards Owned")
    input_wildcards: str = Field(alias="Wildcards")
    input_lifetime_clan_morale: str = Field(alias="Lifetime Clan Morale")
    input_solo_raid_world_reached: str = Field(alias="Solo Raid World Reached")

    @property
    def raid_level(self) -> int:
        return int(self.input_raid_level)

    @property
    def raid_damage(self) -> int:
        return int(self.input_raid_damage)

    @property
    def total_raid_experience(self) -> int:
        return int(self.input_total_raid_experience)

    @property
    def total_raid_attacks(self) -> int:
        return int(self.input_total_raid_attacks)

    @property
    def total_raid_card_levels(self) -> int:
        return int(self.input_total_raid_card_levels)

    @property
    def raid_cards_owned(self) -> int:
        return int(self.input_raid_cards_owned)

    @property
    def wildcards(self) -> int:
        return int(self.input_wildcards)

    @property
    def lifetime_clan_morale(self) -> int:
        return int(self.input_lifetime_clan_morale)

    @property
    def solo_raid_world_reached(self) -> int:
        return int(self.input_solo_raid_world_reached)


class ExportArtifact(BaseModel):
    input_enchanted: str = Field(alias="enchanted")
    input_level: str = Field(alias="level")

    @property
    def enchanted(self) -> bool:
        return self.input_enchanted == "True"

    @property
    def level(self) -> float:
        return float(self.input_level)


class ExportSplashStats(BaseModel):
    input_titan_skip: str = Field(alias="Titan Skip")
    input_pet_titan_skip: str = Field(alias="Pet Titan Skip")
    input_heavenly_strike_titan_skip: str = Field(alias="Heavenly Strike Titan Skip")
    input_shadow_clone_titan_skip: str = Field(alias="Shadow Clone Titan Skip")
    input_clanship_titan_skip: str = Field(alias="Clanship Titan Skip")
    input_dagger_titan_skip: str = Field(alias="Dagger Titan Skip")
    input_gold_gun_titan_skip: str = Field(alias="Gold Gun Titan Skip")
    input_stage_skip: str = Field(alias="Stage Skip")
    input_pet_stage_skip: str = Field(alias="Pet Stage Skip")
    input_pet_skill_stage_skip: str = Field(alias="Pet Skill Stage Skip")
    input_dual_pet_stage_skip: str = Field(alias="Dual Pet Stage Skip")
    input_heavenly_strike_stage_skip: str = Field(alias="Heavenly Strike Stage Skip")
    input_shadow_clone_stage_skip: str = Field(alias="Shadow Clone Stage Skip")
    input_clanship_stage_skip: str = Field(alias="Clanship Stage Skip")
    input_dagger_stage_skip: str = Field(alias="Dagger Stage Skip")
    input_dagger_target_stage_skip: str = Field(alias="Dagger Target Stage Skip")
    input_blade_stream_target_stage_skip: str = Field(alias="Blade Stream Target Stage Skip")
    input_magnum_opus_stage_skip: str = Field(alias="Magnum Opus Stage Skip")
    input_golden_missile_stage_skip: str = Field(alias="Golden Missile Stage Skip")
    input_twilight_fairy_stage_skip: str = Field(alias="Twilight Fairy Stage Skip")

    @property
    def titan_skip(self) -> float:
        return float(self.input_titan_skip)

    @property
    def pet_titan_skip(self) -> float:
        return float(self.input_pet_titan_skip)

    @property
    def heavenly_strike_titan_skip(self) -> float:
        return float(self.input_heavenly_strike_titan_skip)

    @property
    def shadow_clone_titan_skip(self) -> float:
        return float(self.input_shadow_clone_titan_skip)

    @property
    def clanship_titan_skip(self) -> float:
        return float(self.input_clanship_titan_skip)

    @property
    def dagger_titan_skip(self) -> float:
        return float(self.input_dagger_titan_skip)

    @property
    def gold_gun_titan_skip(self) -> float:
        return float(self.input_gold_gun_titan_skip)

    @property
    def stage_skip(self) -> float:
        return float(self.input_stage_skip)

    @property
    def pet_stage_skip(self) -> float:
        return float(self.input_pet_stage_skip)

    @property
    def pet_skill_stage_skip(self) -> float:
        return float(self.input_pet_skill_stage_skip)

    @property
    def dual_pet_stage_skip(self) -> float:
        return float(self.input_dual_pet_stage_skip)

    @property
    def heavenly_strike_stage_skip(self) -> float:
        return float(self.input_heavenly_strike_stage_skip)

    @property
    def shadow_clone_stage_skip(self) -> float:
        return float(self.input_shadow_clone_stage_skip)

    @property
    def clanship_stage_skip(self) -> float:
        return float(self.input_clanship_stage_skip)

    @property
    def dagger_stage_skip(self) -> float:
        return float(self.input_dagger_stage_skip)

    @property
    def dagger_target_stage_skip(self) -> float:
        return float(self.input_dagger_target_stage_skip)

    @property
    def blade_stream_target_stage_skip(self) -> float:
        return float(self.input_blade_stream_target_stage_skip)

    @property
    def magnum_opus_stage_skip(self) -> float:
        return float(self.input_magnum_opus_stage_skip)

    @property
    def golden_missile_stage_skip(self) -> float:
        return float(self.input_golden_missile_stage_skip)

    @property
    def twilight_fairy_stage_skip(self) -> float:
        return float(self.input_twilight_fairy_stage_skip)


class ExportRaidCard(BaseModel):
    level: int
    cards: int


class ExportPassiveSkills(BaseModel):
    intimidating_presence: int = Field(alias="Intimidating Presence")
    power_surge: int = Field(alias="Power Surge")
    anti_titan_cannon: int = Field(alias="Anti-Titan Cannon")
    mystical_iImpact: int = Field(alias="Mystical Impact")
    arcane_bargain: int = Field(alias="Arcane Bargain")
    silent_march: int = Field(alias="Silent March")
    cloak_and_dagger: int = Field(alias="Cloak And Dagger")
    golden_forge: int = Field(alias="Golden Forge")


class ExportMonument(BaseModel):
    input_enchanted: str = Field(alias="enchanted")
    input_level: str = Field(alias="level")

    @property
    def enchanted(self) -> bool:
        return self.input_enchanted == "True"

    @property
    def level(self) -> float:
        return float(self.input_level)


class PlayerExport(BaseModel):
    player_stats: ExportPlayerStats = Field(alias="playerStats")
    raid_stats: ExportRaidStats = Field(alias="raidStats")
    artifacts: dict[model_type.Artifact, ExportArtifact]
    splash_stats: ExportSplashStats = Field(alias="splashStats")
    raid_cards: dict[model_type.ExportCard, ExportRaidCard] = Field(alias="raidCards")
    equipment_sets: tuple[model_type.Equipment, ...] = Field(alias="equipmentSets")
    passive_skills: ExportPassiveSkills = Field(alias="passiveSkills")
    pet_levels: dict[model_type.Pet, int] = Field(alias="petLevels")
    monuments: dict[model_type.Monument, ExportMonument] = Field(alias="monuments")
    skill_tree: dict[model_type.Skill, int] = Field(alias="skillTree")
