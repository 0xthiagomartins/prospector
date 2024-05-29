import whois

domain = "example.com"
data = whois.whois(domain)


"""
data = {
    'domain_name': 'TIHUNTING.COM', 
    'registrar': 'PDR Ltd. d/b/a PublicDomainRegistry.com', 
    'whois_server': 'whois.publicdomainregistry.com', 
    'referral_url': None, 
    'updated_date': [
        datetime.datetime(2024, 3, 13, 19, 21, 27), 
        datetime.datetime(2024, 3, 13, 19, 21, 28)
        ], 
    'creation_date': datetime.datetime(2023, 4, 14, 20, 18, 15), 
    'expiration_date': datetime.datetime(2025, 4, 14, 20, 18, 15), 
    'name_servers': [
        'NSPRO94.HOSTGATOR.COM.BR', 
        'NSPRO95.HOSTGATOR.COM.BR', 
        'nspro94.hostgator.com.br', 
        'nspro95.hostgator.com.br'
        ], 
    'status': 'clientTransferProhibited https://icann.org/epp#clientTransferProhibited', 
    'emails': [
        'abuse-contact@publicdomainregistry.com', 
        'contact@privacyprotect.org'
        ], 
    'dnssec': [
        'unsigned', 
        'Unsigned'
        ], 
    'name': 'Domain Admin', 
    'org': 'Privacy Protect, LLC (PrivacyProtect.org)', 
    'address': '10 Corporate Drive', 
    'city': 'Burlington', 
    'state': 'MA', 
    'registrant_postal_code': '01803', 
    'country': 'US'
}

"""
