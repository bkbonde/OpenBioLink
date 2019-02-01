from graph_creation.file_processor.fileProcessor import FileProcessor
from graph_creation.Types.readerType import ReaderType
from graph_creation.Types.infileType import InfileType
from graph_creation.metadata_infile.edge.inMetaEdgeBgeeOverExpr import InMetaEdgeBgeeOverExpr


class EdgeBgeeOverExprProcessor(FileProcessor):

    def __init__(self):
        self.MetaInfileClass = InMetaEdgeBgeeOverExpr
        self.use_cols =   self.MetaInfileClass.USE_COLS
        super().__init__(self.use_cols, readerType=ReaderType.READER_EDGE_BGEE_DIFF,
                         infileType=InfileType.IN_EDGE_BGEE_OVEREXPR, mapping_sep= self.MetaInfileClass.MAPPING_SEP)

    def individual_preprocessing(self, data):
        data = data[data.differential_expr == 'over-expression']
        return data