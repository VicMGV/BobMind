from profiles.doctor import DoctorProfile
from profiles.researcher import ResearcherProfile

PROFILES = {
    "doctor": DoctorProfile(),
    "researcher": ResearcherProfile()
}

__all__ = ["PROFILES", "DoctorProfile", "ResearcherProfile"]

# Made with Bob
