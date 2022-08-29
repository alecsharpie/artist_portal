import pandas as pd


def get_imgsynth_studies_artists():

    studies_google_sheet = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/1lSvze0VXc-Y-ZduDliueLs0Ue_BbEOCndG4znPp3fHg/export?format=csv&gid=0',
        skiprows=3)

    studies_csv = studies_google_sheet.copy()

    studies_df = studies_csv.iloc[:, 0:13]

    # clean column names
    studies_df.columns = ['last_name', 'first_name',
       'recognized_disco', 'complete_disco', 'recognized_stable', 'complete_stable',
       'tags', 'year_of_death', 'user', 'sgl_img_folder',
       'cards_folder', 'batch_id', 'notes']

    studies_df.fillna("", inplace = True)

    studies_df.loc[:, 'key'] = studies_df.apply(
                       lambda row: f"{row['first_name']} {row['last_name']}",
                       axis=1).str.strip().str.replace(' ', '_')

    studies_df.loc[:,'prompt'] = studies_df.apply(
                       lambda row: f"{row['first_name']} {row['last_name']}",
                       axis=1).str.strip()

    print('Number of artists:', len(studies_df))

    return studies_df
