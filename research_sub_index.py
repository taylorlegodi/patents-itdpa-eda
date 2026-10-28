import pandas as pd

BASE = "clean-pt2/"
PUB_FIELD = "All"    # replace with the AI field name if one exists
PAT_FIELD = "All"    # replace with the AI field name if one exists
YEARS = list(range(2018, 2025))

pubs = pd.read_csv(BASE + "publications_yearly_articles_6countries.csv")
pat = pd.read_csv(BASE + "patents_yearly_applications_6countries.csv")
pop = pd.read_csv(BASE + "population_6countries.csv")

print("Publication fields:", pubs["field"].unique())
print("Patent fields:", pat["field"].unique())

pubs = pubs[(pubs["field"] == PUB_FIELD) & pubs["year"].isin(YEARS)]
pat = pat[(pat["field"] == PAT_FIELD) & pat["year"].isin(YEARS)]

merged = (
    pop[["country", "year", "population"]]
    .merge(pubs[["country", "year", "num_articles"]], on=["country", "year"], how="left")
    .merge(pat[["country", "year", "num_patent_applications"]], on=["country", "year"], how="left")
)

out = merged.rename(columns={
    "num_articles": "ai_publications",
    "num_patent_applications": "ai_patents",
})[["country", "year", "ai_publications", "ai_patents", "population"]]

print("Rows:", len(out), "(expect 42)")
print("Missing values per column:")
print(out.isna().sum())

out.to_csv(BASE + "research_input.csv", index=False)
print("Saved to", BASE + "research_input.csv")