from graph_creation.metadata_db_file.edge.dbMetadataEdge import DbMetadataEdge
from graph_creation.dbType import DbType


class DbMetaEdgeHpa(DbMetadataEdge):
    URL = "https://www.proteinatlas.org/download/rna_tissue.tsv.zip"
    OFILE_NAME = "HPA_gene_anatomy.tsv.zip"
    COLS = ['geneID', 'geneName', 'anatomy', 'expressionValue', 'Unit']
    FILTER_COLS = ['geneID', 'anatomy', 'expressionValue']
    HEADER = 1
    DB_TYPE = DbType.DB_EDGE_HPA

    def __init__(self):
        super().__init__(url= DbMetaEdgeHpa.URL,
                         ofile_name=DbMetaEdgeHpa.OFILE_NAME,
                         dbType= DbMetaEdgeHpa.DB_TYPE)