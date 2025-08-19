import typer

app = typer.Typer(help="LeafLedger: track and review your cigars")

@app.command()
def init(db_path: str = "cigars.db"):
    """Initialize the local database."""
    typer.echo(f"Database initialized at {db_path}")

@app.command()
def add(brand: str, rating: int, notes: str = ""):
    """Add a cigar review."""
    typer.echo(f"Added cigar: {brand} | Rating: {rating} | Notes: {notes}")