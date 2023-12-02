import whois

domains = [
    "GiftGlobeSphere.com",
    "PrestoPresents.com",
    "GiftVoyageHQ.com",
    "MosaicGiftMarket.com",
    "GlobeGifter.com",
    "WishWorldly.com",
    "GiftQuestGlobal.com",
    "EchoGifts.com",
    "ZestGifts.com",
    "GiftGlider.com",
    "VivaGiftsVault.com",
    "GlobalGleamGifts.com",
    "GiftAvenueGlobal.com",
    "ZenithGiftZones.com",
    "GiftLinx.com",
    "GiftPulsePlanet.com",
    "OrbitGiftOasis.com",
    "GiftSphereUniversal.com",
    "GalacticGiftGallery.com",
    "GiftHavenHub.com",
    "GlobalGiftsGala.com",
    "GiftExplorerWorld.com",
    "UniversalGiftUniverse.com",
    "GiftOdysseyGlobal.com",
    "GiftsCosmoConnect.com",
    "PlanetPresentPicks.com",
    "GalaxyGiftGateway.com",
    "CelestialGiftCircle.com",
    "GiftsOrbitZone.com",
    "GiftGalaxyVenture.com",
    "GiftingSphereWorld.com",
    "WanderlustGiftsWorld.com",
    "GiftJourneyGlobal.com",
    "GiftNovaNetwork.com",
    "CosmicGiftsCorner.com",
    "GlobalGiftsVoyager.com",
    "InterstellarGiftIdeas.com",
    "GiftsPlanetarium.com",
    "UniversalGiftingHub.com",
    "GiftsBeyondBorders.com",
    "GiftsCosmicCrate.com",
    "GiftGlobeJunction.com",
    "UniversalGiftStation.com",
    "GiftsStellarSpot.com",
    "GlobalGiftsOdyssey.com",
    "CosmoGiftsCollection.com",
    "GiftsUniversalPath.com",
    "GlobalGiftsFiesta.com",
    "GiftsInfinityHub.com",
    "CelestialGiftsBazaar.com"
]


for domain in domains:
    try:
        domain_info = whois.whois(domain)
        if domain_info.domain_name is None:
            print(f"{domain} is available!")
        else:
            print(f"{domain} is already taken.")
    except whois.parser.PywhoisError as e:  # Catching specific whois error
        if "No match for" in str(e):
            print(f"{domain} is available!")
        else:
            print(f"Error checking {domain}: {e}")
