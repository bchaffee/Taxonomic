from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Kingdom, Base, Phyla, User
engine = create_engine('sqlite:///kingdomphyla.db')


# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Brandon Chaffee",
             email="brandon.c.chaffee@gmail.com",
             picture='http://i2.cdn.turner.com/cnnnext/dam/assets\
             /140808122043-01-selfie-monkey-0808-exlarge-169.jpeg')
session.add(User1)
session.commit()

# Creates an instance for aniamlia kingdom
kingdom1 = Kingdom(user_id=1, name="Animilia")

session.add(kingdom1)
session.commit()


phyla1 = Phyla(user_id=1,
               name="Acanthocephala",
               meaning="Thorny headed worms",
               characteristic="Reversible spiny proboscis. Now usually \
               included in Rotifera.",
               kingdom=kingdom1)

session.add(phyla1)
session.commit()

phyla2 = Phyla(user_id=1,
               name="Acoelomorpha",
               meaning="Without gut",
               characteristic="No mouth or alimentary canal (alimentary canal\
               = digestive tract in digestive system)",
               kingdom=kingdom1)

session.add(phyla2)
session.commit()

phyla3 = Phyla(user_id=1,
               name="Annelida",
               meaning="Little ring",
               characteristic="Multiple circular segment",
               kingdom=kingdom1)

session.add(phyla3)
session.commit()

phyla4 = Phyla(user_id=1,
               name="Arthropoda",
               meaning="Jointed foot",
               characteristic="Chitin exoskeleton",
               kingdom=kingdom1)

session.add(phyla4)
session.commit()

# Creates an instance for plantae kingdom
kingdom2 = Kingdom(user_id=1, name="Plantae")

session.add(kingdom2)
session.commit()

phyla1 = Phyla(user_id=1,
               name="Anthocerotophyta",
               meaning="Anthoceros-like plants",
               characteristic="horn-shaped sporophytes, no vascular system",
               kingdom=kingdom2)

session.add(phyla1)
session.commit()

phyla2 = Phyla(user_id=1,
               name="Bryophyta",
               meaning="Bryum-like plants, moss plants",
               characteristic="persistent unbranched sporophytes,\
               no vascular system",
               kingdom=kingdom2)

session.add(phyla2)
session.commit()

phyla3 = Phyla(user_id=1,
               name="Marchantiophyta",
               meaning="Marchantia-like plants liver plants",
               characteristic="ephemeral unbranched sporophytes,\
               no vascular system",
               kingdom=kingdom2)

session.add(phyla3)
session.commit()

phyla4 = Phyla(user_id=1,
               name="Lycopodiophyta",
               meaning="Lycopodium-like plants wolf plants",
               characteristic="microphyll leaves, vascular system",
               kingdom=kingdom2)

session.add(phyla4)
session.commit()


# Creates an instance for fungie kingdom
kingdom3 = Kingdom(user_id=1, name="Fungie")

session.add(kingdom3)
session.commit()

phyla1 = Phyla(user_id=1,
               name="Neolectomycetes",
               meaning="Earth tongues",
               characteristic="weakly clusters with a bizarre group of\
               basal Ascomycota",
               kingdom=kingdom3)

session.add(phyla1)
session.commit()

phyla2 = Phyla(user_id=1,
               name="Pneumocystidomycetes",
               meaning="??",
               characteristic="??",
               kingdom=kingdom3)

session.add(phyla2)
session.commit()

phyla3 = Phyla(user_id=1,
               name="Schizosaccharomycetes",
               meaning="??",
               characteristic="??",
               kingdom=kingdom3)

session.add(phyla3)
session.commit()

# Creates an instance for protista kingdom
kingdom4 = Kingdom(user_id=1, name="Protista")

session.add(kingdom4)
session.commit()

phyla1 = Phyla(user_id=1,
               name="Euglenozoa",
               meaning="Protozoa",
               characteristic="may have formed by endosymbiosis \
               (engulfed green algae cell)",
               kingdom=kingdom4)

session.add(phyla1)
session.commit()

phyla2 = Phyla(user_id=1,
               name="Sarcodina",
               meaning="Protozoa",
               characteristic="Amoeba, radiolarians",
               kingdom=kingdom4)

session.add(phyla2)
session.commit()

phyla3 = Phyla(user_id=1,
               name=" Ciliophora",
               meaning="Protozoa",
               characteristic="Paramecium, Blepharisma",
               kingdom=kingdom4)

session.add(phyla3)
session.commit()

phyla4 = Phyla(user_id=1,
               name="Phaeophyta",
               meaning="Algae",
               characteristic="brown algae (Fucus)",
               kingdom=kingdom4)

session.add(phyla4)
session.commit()

# Creates an instance for archaea kingdom
kingdom5 = Kingdom(user_id=1, name="Archaea")

session.add(kingdom5)
session.commit()

phyla1 = Phyla(user_id=1,
               name="Crenarchaeota",
               meaning="",
               characteristic="",
               kingdom=kingdom5)

session.add(phyla1)
session.commit()

phyla2 = Phyla(user_id=1,
               name="Euryarchaeota",
               meaning="",
               characteristic="",
               kingdom=kingdom5)

session.add(phyla2)
session.commit()

phyla3 = Phyla(user_id=1,
               name="Korarchaeota",
               meaning="koros or kore, meaning young man",
               characteristic="deeply branching lineage that does not belong \
               to the main archaeal groups",
               kingdom=kingdom5)

session.add(phyla3)
session.commit()

phyla4 = Phyla(user_id=1,
               name="Lokiarchaeota",
               meaning="sample was taken near a hydrothermal vent\
               at a site known as Loki's Castle",
               characteristic="unicellular life dubbed Lokiarchaeum",
               kingdom=kingdom5)

session.add(phyla4)
session.commit()

# Creates an instance for bacteria kingdom
kingdom6 = Kingdom(user_id=1, name="Bacteria")

session.add(kingdom6)
session.commit()

phyla1 = Phyla(user_id=1,
               name="Acidobacteria",
               meaning="diderm Gram negative",
               characteristic="abundant bacterial phylum in many soils,\
               but its members are mostly uncultured",
               kingdom=kingdom6)

session.add(phyla1)
session.commit()

phyla2 = Phyla(user_id=1,
               name="Chlamydiae",
               meaning="diderms, weakly Gram negative",
               characteristic="composed of only 6 genera of obligate\
               intracellular pathogens with a complex life cycle",
               kingdom=kingdom6)

session.add(phyla2)
session.commit()

phyla3 = Phyla(user_id=1,
               name="Chlorobi",
               meaning="known colloquially as Green sulfur bacteria",
               characteristic="ontains only 7 genera of obligately anaerobic\
               photoautotrophic bacteria",
               kingdom=kingdom6)

session.add(phyla3)
session.commit()

phyla4 = Phyla(user_id=1,
               name="Firmicutes",
               meaning="firmus, strong, and cutis, skin, referring to the\
               cell wall",
               characteristic="Low-G+C Gram positive species most often\
               spore-forming, in two/three classes",
               kingdom=kingdom6)

session.add(phyla4)
session.commit()

print "added Kingdoms and Phyla items!"
