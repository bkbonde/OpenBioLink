from ....edgeType import EdgeType
from ...types.infileType import InfileType
from ...metadata_infile.infileMetadata import InfileMetadata
from ....nodeType import NodeType


class InMetaEdgeStringPtmod(InfileMetadata):
    CSV_NAME = "DB_STRING_gene_ptmod_gene.csv"
    USE_COLS = ['item_id_a', 'item_id_b', 'score']
    NODE1_COL = 0
    NODE2_COL = 1
    QSCORE_COL = 2
    NODE1_TYPE = NodeType.GENE
    NODE2_TYPE = NodeType.GENE
    EDGE_TYPE = EdgeType.GENE_PTMOD_GENE
    INFILE_TYPE = InfileType.IN_EDGE_STRING_PTMOD


    MAPPING_SEP = None

    def __init__(self):
        super().__init__(csv_name=self.CSV_NAME,
                         cols=self.USE_COLS,
                         infileType=self.INFILE_TYPE)