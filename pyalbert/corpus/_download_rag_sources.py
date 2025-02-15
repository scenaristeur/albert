import json
import os
import shutil
from urllib.error import HTTPError

import wget


def download_rag_sources(storage_dir: str, config_file: str):
    """Download french data corpus that power the RAG system.
       Overwrite data if they already exist.

    Args:
        storage_dir (str): path where to download the directory
        config_file (str,): configuration path file.
    """

    # create the storage path if it does not exist
    os.makedirs(storage_dir, exist_ok=True)
    os.makedirs(f"{storage_dir}/data.gouv", exist_ok=True)

    with open(config_file) as f:
        coprus_config = json.load(f)

    for corpus_id, corpus in coprus_config.items():
        print(f"Dowloading '{corpus_id}'...\n")
        last_name = corpus["url"].split("/")[-1]
        target = f"{storage_dir}/{corpus['output']}"
        try:
            wget.download(corpus["url"], f"{storage_dir}/temp_{last_name}")
        except HTTPError as err:
            print(f"Error: {err}")
            print(f'Failed to fetch source {corpus_id} from {corpus["url"]}')
            continue
        if corpus.get("format"):
            shutil.unpack_archive(
                f"{storage_dir}/temp_{last_name}", extract_dir=target, format=corpus["format"]
            )
        else:
            shutil.move(f"{storage_dir}/temp_{last_name}", target)
        print()

    print("\nCorpus files successfuly downloaded")
