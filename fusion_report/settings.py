import os

from typing import Any, Dict


class Settings:

    ROOT_DIR: str = os.path.dirname(os.path.abspath(__file__))
    VERSION: str = '2.1.4'
    DATE_FORMAT: str = '%d/%m/%Y'
    THREAD_NUM: int = 2
    FUSION_WEIGHTS: Dict[str, float] = {
        'fusiongdb': 0.20, 
        'cosmic': 0.40, 
        'mitelman': 0.40
    }

    COSMIC: Dict[str, str] = {
        'NAME': 'COSMIC',
        'HOSTNAME': 'https://cancer.sanger.ac.uk/cosmic/file_download/GRCh38/cosmic/v87',
        'SCHEMA': 'Cosmic.sql',
        'FILE': 'CosmicFusionExport.tsv.gz'
    }

    FUSIONGDB: Dict[str, Any] = {
        'NAME': 'FusionGDB',
        'SCHEMA': 'FusionGDB.sql',
        'HOSTNAME': 'https://ccsm.uth.edu/FusionGDB/tables',
        'FILES': [
            'TCGA_ChiTaRS_combined_fusion_information_on_hg19.txt',
            'TCGA_ChiTaRS_combined_fusion_ORF_analyzed_gencode_h19v19.txt',
            'uniprot_gsymbol.txt',
            'fusion_uniprot_related_drugs.txt',
            'fusion_ppi.txt',
            'fgene_disease_associations.txt'
        ]
    }

    MITELMAN: Dict[str, str] = {
        'NAME': 'Mitelman',
        'SCHEMA': 'Mitelman.sql',
        'HOSTNAME': 'ftp://ftp1.nci.nih.gov/pub/CGAP',
        'FILE': 'mitelman.tar.gz'
    }

    SOURCEFORGE: Dict[str, str] = {
        'HOSTNAME': 'https://downloads.sourceforge.net/project/fusion-report-db/20-04-2020/',
        'FILE': 'db.tar.gz'
    }
