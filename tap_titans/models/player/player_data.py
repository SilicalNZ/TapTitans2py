from tap_titans.utils.base import Struct, field

from tap_titans.models.player import Artifacts, Card, ClanScrolls, HeroWeapons, Pets


class PlayerArtifact(Struct):
    artifact_id: Artifacts
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
    scroll_id: ClanScrolls = field(name="ScrollId")


class PlayerHeroWeapon(Struct):
    level: int = field(name="Level")
    hero_id: HeroWeapons = field(name="HelperID")


class PlayerPet(Struct):
    level: int
    pet_id: Pets


class PlayerSeasonalArtifact(Struct):
    artifact_id: str
    is_enchanted: bool
    level: str


class PlayerSkill(Struct):
    level: int
    skill_id: str


class PlayerData(Struct):
    additive_relic_multiplier: int | None
    artifacts: tuple[PlayerArtifact, ...] | None
    badge_count: PlayerBadgeCount | None
    cards: tuple[PlayerCard, ...] | None
    challenge_tournaments_participation: int | None
    challenge_tournaments_undisputed_count: int | None
    clan_code: str | None
    clan_name: str | None
    clan_scroll: tuple[PlayerClanScroll, ...] | None
    country_code: str | None
    crafting_shards_spent: int | None
    current_card_currency: int | None
    current_world_id: int | None
    daily_raid_tickets: int | None
    equipment_set: tuple[str, ...] | None
    equipment_set_count: int | None
    hero_weapon: tuple[PlayerHeroWeapon, ...] | None
    loyalty_level: int | None
    max_stage: int | None
    name: str | None
    pets: tuple[PlayerPet, ...] | None
    player_code: str | None
    player_raid_level: int | None
    previous_rank: str | None
    raid_wildcard_count: int | None
    relics_received: str | None
    relics_spent: str | None
    role: str | None
    seasonal_artifacts: tuple[PlayerSeasonalArtifact, ...] | None
    seasonal_relic_multiplier: int | None
    seasonal_relics_received: str | None
    seasonal_relics_spent: str | None
    skill_tree: tuple[PlayerSkill, ...] | None
    titan_points: int | None
    total_card_level: int | None
    total_clan_scrolls: int | None
    total_hero_weapons: int | None = field(name="total_helper_weapons")
    total_pet_levels: int | None
    total_raid_player_xp: int | None
    total_skill_points: int | None
    total_tournaments: int | None
    undisputed_count: int | None
    weekly_ticket_count: int | None
