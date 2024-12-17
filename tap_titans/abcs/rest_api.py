import abc
from dataclasses import dataclass
from enum import Enum

from tap_titans.models.generic import ClanCode
from tap_titans.abcs.error import UnknownError
from tap_titans.utils.base import Struct, field
from tap_titans.models.player import PlayerData, PlayerRaidResearchTree, PlayerCard, PlayerRaidResearchBonuses


__all__ = (
    "RestAPIABC",
    "RaidRestABC",
    "SubscribeResp",
    "SubscribeRespOK",
    "SubscribeRespRefused",
    "UnknownError",
    "ClanDataResp",
    "ClanDataProperties",
    "PlayerDataProperties",
)


class SubscribeRespOKMember(Struct):
    name: str
    player_code: str


class SubscribeRespOK(Struct):
    token: str
    clan_code: ClanCode
    clan_name: str
    member_list: list[SubscribeRespOKMember]


class SubscribeRespRefused(Struct):
    token: str
    reason: str


class SubscribeResp(Struct):
    ok: tuple[SubscribeRespOK, ...]
    refused: tuple[SubscribeRespRefused, ...]


class ClanPlayerData(Struct):
    player_code: str | None = field(default=None)
    country_code: str | None = field(default=None)
    max_stage: int | None = field(default=None)
    raid_wildcard_count: int | None = field(default=None)
    current_card_currency: int | None = field(default=None)
    name: str | None = field(default=None)
    total_raid_player_xp: int | None = field(default=None)
    player_raid_level: int | None = field(default=None)
    summon_level: int | None = field(default=None)
    total_card_level: int | None = field(default=None)
    role: str | None = field(default=None)
    weekly_ticket_count: int | None = field(default=None)
    # titan_cards is excluded since it's a mistake by GameHive to include it and slows down the .all() by a lot
    raid_research_tree: PlayerRaidResearchTree | None = field(default=None)
    raid_research_bonuses: PlayerRaidResearchBonuses | None = field(default=None)
    loyalty_level: int | None = field(default=None)
    daily_raid_tickets: int | None = field(default=None)
    previous_rank: str | None = field(default=None)
    summon_level: int | None = field(default=None)
    cards: tuple[PlayerCard, ...] | None = field(default=None)
    equipment_set: tuple[str, ...] | None = field(default=None)


class ClanDataResp(Struct):
    clan_name: str
    clan_code: ClanCode
    players_data: tuple[ClanPlayerData, ...]


class ClanDataProperties(str, Enum):
    max_stage = "max_stage"
    player_code = "player_code"
    country_code = "country_code"
    raid_wildcard_count = "raid_wildcard_count"
    current_card_currency = "current_card_currency"
    name = "name"
    total_raid_player_xp = "total_raid_player_xp"
    player_raid_level = "player_raid_level"
    summon_level = "summon_level"
    total_card_level = "total_card_level"
    role = "role"
    weekly_ticket_count = "weekly_ticket_count"
    # titan_cards is excluded since it's a mistake by GameHive to include it and slows down the .all() by a lot
    raid_research_tree = "raid_research_tree"
    raid_research_bonuses = "raid_research_bonuses"
    loyalty_level = "loyalty_level"
    daily_raid_tickets = "daily_raid_tickets"
    previous_rank = "previous_rank"
    cards = "cards"
    equipment_set = "equipment_set"

    @classmethod
    def all(cls) -> tuple['ClanDataProperties', ...]:
        return cls._member_map_.values()


class PlayerDataProperties(str, Enum):
    player_code = "player_code"
    country_code = "country_code"
    max_stage = "max_stage"
    crafting_shards_spent = "crafting_shards_spent"
    raid_wildcard_count = "raid_wildcard_count"
    current_card_currency = "current_card_currency"
    additive_relic_multiplier = "additive_relic_multiplier"
    relics_received = "relics_received"
    relics_spent = "relics_spent"
    summon_level = "summon_level"
    name = "name"
    total_tournaments = "total_tournaments"
    undisputed_count = "undisputed_count"
    titan_points = "titan_points"
    total_raid_player_xp = "total_raid_player_xp"
    player_raid_level = "player_raid_level"
    total_card_level = "total_card_level"
    equipment_set_count = "equipment_set_count"
    total_pet_levels = "total_pet_levels"
    total_skill_points = "total_skill_points"
    total_helper_weapons = "total_helper_weapons"
    total_clan_scrolls = "total_clan_scrolls"
    challenge_tournaments_participation = "challenge_tournaments_participation"
    challenge_tournaments_undisputed_count = "challenge_tournaments_undisputed_count"
    current_world_id = "current_world_id"
    clan_code = "clan_code"
    clan_name = "clan_name"
    role = "role"
    weekly_ticket_count = "weekly_ticket_count"
    titan_cards = "titan_cards"
    raid_research_tree = "raid_research_tree"
    raid_research_bonuses = "raid_research_bonuses"
    loyalty_level = "loyalty_level"
    daily_raid_tickets = "daily_raid_tickets"
    previous_rank = "previous_rank"
    artifacts = "artifacts"
    seasonal_relics_received = "seasonal_relics_received"
    seasonal_relics_spent = "seasonal_relics_spent"
    seasonal_relic_multiplier = "seasonal_relic_multiplier"
    seasonal_artifacts = "seasonal_artifacts"
    cards = "cards"
    pets = "pets"
    badge_count = "badge_count"
    hero_weapon = "hero_weapon"
    clan_scroll = "clan_scroll"
    skill_tree = "skill_tree"
    equipment_set = "equipment_set"

    @classmethod
    def all(cls) -> tuple['PlayerDataProperties', ...]:
        return cls._member_map_.values()


@dataclass
class RestAPIABC(metaclass=abc.ABCMeta):
    # https://tt2-docs.gamehivegames.com/rest/

    @abc.abstractmethod
    async def subscribe(self, player_tokens: list[str]) -> SubscribeResp | UnknownError:
        raise NotImplementedError()

    @abc.abstractmethod
    async def unsubscribe(self, player_tokens: list[str]) -> SubscribeResp | UnknownError:
        raise NotImplementedError()

    @abc.abstractmethod
    async def clan_data(self, player_token: str, properties: tuple[ClanDataProperties, ...]) -> ClanDataResp | UnknownError:
        raise NotImplementedError()

    @abc.abstractmethod
    async def player_data(self, player_token: str, properties: tuple[PlayerDataProperties, ...]) -> PlayerData | UnknownError:
        raise NotImplementedError()
