from tap_titans.utils.base import Struct, field

from tap_titans.models.player import Artifacts, Card, ClanScrolls, HeroWeapons, Pets


class PlayerArtifact(Struct):
    artifact_id: str
    is_enchanted: bool
    level: str


class PlayerBadgeCount(Struct):
    zero: int = field(name="0")
    one: int = field(name="1")
    two: int = field(name="2")
    three: int = field(name="3")
    four: int = field(name="4")


class PlayerCard(Struct):
    level: int
    quantity_received: int
    quantity_spent: int
    skill_name: Card


class PlayerClanScroll(Struct):
    level: int = field(name="Level")
    scroll_id: str = field(name="ScrollId")


class PlayerHeroWeapon(Struct):
    level: int = field(name="Level")
    hero_id: str = field(name="HelperID")


class PlayerPet(Struct):
    level: int
    pet_id: str


class PlayerSeasonalArtifact(Struct):
    artifact_id: str
    is_enchanted: bool
    level: str


class PlayerSkill(Struct):
    level: int
    skill_id: str


class PlayerTitanCard(Struct):
    titan_id: str
    level: int
    quantity_received: int
    quantity_spent: int


class PlayerRaidResearchTree(Struct):
    armor_damage: float | None = field(name="ArmorDamage", default=None)
    body_damage: float | None = field(name="BodyDamage", default=None)
    chest_damage: float | None = field(name="ChestDamage", default=None)
    head_damage: float | None = field(name="HeadDamage", default=None)
    limb_damage: float | None = field(name="LimbDamage", default=None)
    raid_enemy_1_damage: float | None = field(name="RaidEnemy1Damage", default=None)
    raid_enemy_2_damage: float | None = field(name="RaidEnemy2Damage", default=None)
    raid_enemy_3_damage: float | None = field(name="RaidEnemy3Damage", default=None)
    raid_enemy_4_damage: float | None = field(name="RaidEnemy4Damage", default=None)
    raid_enemy_5_damage: float | None = field(name="RaidEnemy5Damage", default=None)
    raid_enemy_6_damage: float | None = field(name="RaidEnemy6Damage", default=None)
    raid_enemy_7_damage: float | None = field(name="RaidEnemy7Damage", default=None)
    raid_enemy_8_damage: float | None = field(name="RaidEnemy8Damage", default=None)


class PlayerRaidResearchBonuses(Struct):
    raid_base_damage: float | None = field(name="RaidBaseDamage", default=None)
    affliction_base_damage: float | None = field(name="AfflictionBaseDamage", default=None)
    burst_base_damage: float | None = field(name="BurstBaseDamage", default=None)
    armor_base_damage: float | None = field(name="ArmorBaseDamage", default=None)
    body_base_damage: float | None = field(name="BodyBaseDamage", default=None)
    head_base_damage: float | None = field(name="HeadBaseDamage", default=None)
    limb_base_damage: float | None = field(name="LimbBaseDamage", default=None)
    torso_base_damage: float | None = field(name="TorsoBaseDamage", default=None)
    head_armor_base_damage: float | None = field(name="HeadArmorBaseDamage", default=None)
    limb_armor_base_damage: float | None = field(name="LimbArmorBaseDamage", default=None)
    torso_armor_base_damage: float | None = field(name="TorsoArmorBaseDamage", default=None)
    head_body_base_damage: float | None = field(name="HeadBodyBaseDamage", default=None)
    limb_body_base_damage: float | None = field(name="LimbBodyBaseDamage", default=None)
    torso_body_base_damage: float | None = field(name="TorsoBodyBaseDamage", default=None)
    enemy_1_base_damage: float | None = field(name="Enemy1BaseDamage", default=None)
    enemy_2_base_damage: float | None = field(name="Enemy2BaseDamage", default=None)
    enemy_3_base_damage: float | None = field(name="Enemy3BaseDamage", default=None)
    enemy_4_base_damage: float | None = field(name="Enemy4BaseDamage", default=None)
    enemy_5_base_damage: float | None = field(name="Enemy5BaseDamage", default=None)
    enemy_6_base_damage: float | None = field(name="Enemy6BaseDamage", default=None)
    enemy_7_base_damage: float | None = field(name="Enemy7BaseDamage", default=None)
    enemy_8_base_damage: float | None = field(name="Enemy8BaseDamage", default=None)
    enemy_1_affliction_base_damage: float | None = field(name="Enemy1AfflictionBaseDamage", default=None)
    enemy_2_affliction_base_damage: float | None = field(name="Enemy2AfflictionBaseDamage", default=None)
    enemy_3_affliction_base_damage: float | None = field(name="Enemy3AfflictionBaseDamage", default=None)
    enemy_4_affliction_base_damage: float | None = field(name="Enemy4AfflictionBaseDamage", default=None)
    enemy_5_affliction_base_damage: float | None = field(name="Enemy5AfflictionBaseDamage", default=None)
    enemy_6_affliction_base_damage: float | None = field(name="Enemy6AfflictionBaseDamage", default=None)
    enemy_7_affliction_base_damage: float | None = field(name="Enemy7AfflictionBaseDamage", default=None)
    enemy_8_affliction_base_damage: float | None = field(name="Enemy8AfflictionBaseDamage", default=None)
    enemy_1_burst_base_damage: float | None = field(name="Enemy1BurstBaseDamage", default=None)
    enemy_2_burst_base_damage: float | None = field(name="Enemy2BurstBaseDamage", default=None)
    enemy_3_burst_base_damage: float | None = field(name="Enemy3BurstBaseDamage", default=None)
    enemy_4_burst_base_damage: float | None = field(name="Enemy4BurstBaseDamage", default=None)
    enemy_5_burst_base_damage: float | None = field(name="Enemy5BurstBaseDamage", default=None)
    enemy_6_burst_base_damage: float | None = field(name="Enemy6BurstBaseDamage", default=None)
    enemy_7_burst_base_damage: float | None = field(name="Enemy7BurstBaseDamage", default=None)
    enemy_8_burst_base_damage: float | None = field(name="Enemy8BurstBaseDamage", default=None)


class PlayerData(Struct):
    player_code: str | None = field(default=None)
    country_code: str | None = field(default=None)
    max_stage: int | None = field(default=None)
    crafting_shards_spent: int | None = field(default=None)
    raid_wildcard_count: int | None = field(default=None)
    current_card_currency: int | None = field(default=None)
    additive_relic_multiplier: int | None = field(default=None)
    relics_received: str | None = field(default=None)
    relics_spent: str | None = field(default=None)
    summon_level: int | None = field(default=None)
    name: str | None = field(default=None)
    total_tournaments: int | None = field(default=None)
    undisputed_count: int | None = field(default=None)
    titan_points: str | None = field(default=None)
    total_raid_player_xp: int | None = field(default=None)
    player_raid_level: int | None = field(default=None)
    total_card_level: int | None = field(default=None)
    equipment_set_count: int | None = field(default=None)
    total_pet_levels: int | None = field(default=None)
    total_skill_points: int | None = field(default=None)
    total_clan_scrolls: int | None = field(default=None)
    challenge_tournaments_participation: int | None = field(default=None)
    challenge_tournaments_undisputed_count: int | None = field(default=None)
    current_world_id: int | None = field(default=None)
    clan_code: str | None = field(default=None)
    clan_name: str | None = field(default=None)
    role: str | None = field(default=None)
    weekly_ticket_count: int | None = field(default=None)
    titan_cards: tuple[PlayerTitanCard, ...] | None = field(default=None)
    raid_research_tree : PlayerRaidResearchTree | None = field(default=None)
    raid_research_bonuses: PlayerRaidResearchBonuses | None = field(default=None)
    loyalty_level: int | None = field(default=None)
    daily_raid_tickets: int | None = field(default=None)
    previous_rank: str | None = field(default=None)
    artifacts: tuple[PlayerArtifact, ...] | None = field(default=None)
    seasonal_relics_received: str | None = field(default=None)
    seasonal_relics_spent: str | None = field(default=None)
    seasonal_relic_multiplier: int | None = field(default=None)
    seasonal_artifacts: tuple[PlayerSeasonalArtifact, ...] | None = field(default=None)
    cards: tuple[PlayerCard, ...] | None = field(default=None)
    pets: tuple[PlayerPet, ...] | None = field(default=None)
    badge_count: PlayerBadgeCount | None = field(default=None)
    hero_weapon: tuple[PlayerHeroWeapon, ...] | None = field(default=None)
    clan_scroll: tuple[PlayerClanScroll, ...] | None = field(default=None)
    skill_tree: tuple[PlayerSkill, ...] | None = field(default=None)
    equipment_set: tuple[str, ...] | None = field(default=None)
    total_hero_weapons: int | None = field(name="total_helper_weapons", default=None)
