from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

# Conexão com o banco de dados Chinook
engine = create_engine("sqlite:///chinook.db", echo=False)

# Reflete as tabelas
Base = automap_base()
Base.prepare(autoload_with=engine)

# Acessa as classes ORM das tabelas
Track = Base.classes.tracks
Album = Base.classes.albums
InvoiceItem = Base.classes.invoice_items
Artist = Base.classes.artists

# Cria sessão
session = Session(engine)

# 1. Três primeiros registros da tabela tracks
print("\n--- 3 primeiros registros da tabela Tracks ---")
for track in session.scalars(select(Track).limit(3)):
    print(track.TrackId, track.Name, track.UnitPrice)

# 2. Nome da faixa e título do álbum das primeiras 20 faixas
print("\n--- Nome da faixa e título do álbum (20 primeiras) ---")
stmt = select(Track.Name, Album.Title).join(Album, Track.AlbumId == Album.AlbumId).limit(20)
for name, title in session.execute(stmt):
    print(name, "->", title)

# 3. 10 primeiras vendas de faixas na tabela invoice_items
print("\n--- 10 primeiras vendas (Invoice Items) ---")
for item in session.scalars(select(InvoiceItem).limit(10)):
    print(f"InvoiceId: {item.InvoiceId}, TrackId: {item.TrackId}, Qty: {item.Quantity}, Price: {item.UnitPrice}")

# 4. Nomes das faixas vendidas + quantidade (10 primeiras vendas)
print("\n--- Nomes das faixas e quantidade vendida (10 primeiras vendas) ---")
stmt = (
    select(Track.Name, InvoiceItem.Quantity)
    .join(Track, Track.TrackId == InvoiceItem.TrackId)
    .limit(10)
)
for name, qty in session.execute(stmt):
    print(name, "-", qty)

# 5. Top 10 faixas mais vendidas
print("\n--- Top 10 faixas mais vendidas ---")
stmt = (
    select(Track.Name, func.sum(InvoiceItem.Quantity).label("total_vendas"))
    .join(InvoiceItem, Track.TrackId == InvoiceItem.TrackId)
    .group_by(Track.Name)
    .order_by(func.sum(InvoiceItem.Quantity).desc())
    .limit(10)
)
for name, total in session.execute(stmt):
    print(name, "-", total)

# 6. Top 10 artistas que mais venderam
print("\n--- Top 10 artistas mais vendidos ---")
stmt = (
    select(Artist.Name, func.sum(InvoiceItem.Quantity).label("total_vendas"))
    .join(Album, Artist.ArtistId == Album.ArtistId)
    .join(Track, Album.AlbumId == Track.AlbumId)
    .join(InvoiceItem, Track.TrackId == InvoiceItem.TrackId)
    .group_by(Artist.Name)
    .order_by(func.sum(InvoiceItem.Quantity).desc())
    .limit(10)
)
for name, total in session.execute(stmt):
    print(name, "-", total)

# Fecha a sessão
session.close()