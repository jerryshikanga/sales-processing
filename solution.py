import json
import os
import time
import shutil

import pandas as pd


def read_and_concatenate_sales_data(directory="./Data/Sales"):
    column_names = ['identifier', 'Network', 'Region', 'Date', 'Product', 'Amount']
    sales_df = pd.DataFrame(columns=column_names)

    for file_path in os.listdir(directory):
        file_df = pd.read_csv(os.path.join(directory, file_path))
        sales_df = sales_df.append(file_df, ignore_index=True)
    return sales_df


def enrich_sales_data_with_description(sales_df, region_df_path="./Data/Region/region_2016.csv"):
    # Enrich sales data with region description
    region_df = pd.read_csv(region_df_path)
    enriched_df = pd.merge(sales_df, region_df[['Region', 'RegionDescription']], on='Region')
    return enriched_df


def summarize_data_using_region_and_network(enriched_df):
    amount_grouped_df = enriched_df.groupby(by=["Region", "Network"], as_index=False)[['Amount']].sum()
    counts_grouped_df = enriched_df.groupby(by=["Region", "Network"], as_index=False)[['identifier']].count()
    counts_grouped_df.rename(columns={'identifier': 'Total Sales Number'}, inplace=True)

    summary_df = pd.merge(amount_grouped_df, counts_grouped_df, on=['Region', 'Network'])
    return summary_df


def write_output_file_with_totals(summary_df):
    # to prevent overwrite make each file unique by appending a timestamp to the name
    file_name = f"./Data/Output/processed_data_{time.time()}.csv"
    summary_df.to_csv(file_name, index=False)
    return file_name


def archive_processed_sales_data(source="./Data/Sales", destination="./Data/Archive"):
    file_changes = dict()
    for file_name in os.listdir(source):
        source_file = os.path.join(source, file_name)
        destination_file = os.path.join(destination, file_name)
        shutil.move(source_file, destination_file)
        file_changes[source_file] = destination_file
    return file_changes


def main():
    sales_df = read_and_concatenate_sales_data()
    enriched_df = enrich_sales_data_with_description(sales_df)
    summary_df = summarize_data_using_region_and_network(enriched_df)
    file_name = write_output_file_with_totals(summary_df)
    print(f"Saved summary data in {file_name}")
    archived_files = archive_processed_sales_data()
    print(f"Archived Files : {json.dumps(archived_files)}")


if __name__ == "__main__":
    main()
