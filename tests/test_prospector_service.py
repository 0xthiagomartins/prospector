from src.service import Prospector


def test_get_emails_from_domain(domain: str):
    assert Prospector(verbose=True).list_emails_from_domain(
        domain
    ), "Erro ao coletar email"
