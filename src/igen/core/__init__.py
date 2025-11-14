"""Core functions and definitions for igen projects."""

from .domain import HlaAllele, HlaAlleleProtocol, HlaHaplotype, HlaHaplotypeProtocol
from .enum import HlaLocus, HlaLocusChain, HlaLocusEnum, HlaLocusGroup, HlaLocusGroupEnum
from .service import LoggerService
from .singleton import Singleton

__all__ = [
    "Singleton",
    "HlaAllele",
    "HlaAlleleProtocol",
    "HlaHaplotype",
    "HlaHaplotypeProtocol",
    "HlaLocus",
    "HlaLocusChain",
    "HlaLocusEnum",
    "HlaLocusGroup",
    "HlaLocusGroupEnum",
    "LoggerService",
]
