import pytest
from the_movie.movie import find_the_oldest_soundtrack

@pytest.mark.usefixtures("spark_session")
def test_the_oldest_soundtrack(spark_session):
    test_df = spark_session.createDataFrame(
        [
            ('1', 'z',  1990, 2000, 'soundtrack, a', 'w'),
            ('1', 'y',  1990, 2000, 'b', 'z'),
            ('1', 'x',  1780, 1800, 'soundtrack, b', 'e'),
            ('1', 't',  1810, 2000, 'd', 'asd'),
        ],
        ['nconst', 'primaryName', 'birthYear', 'deathYear', 'primaryProfession', 'knownForTitles']
    )
    df_soundtrack= find_the_oldest_soundtrack(test_df)
    assert df_soundtrack == 1780


@pytest.mark.usefixtures("spark_session")
def test_no_soundtrack(spark_session):
    test_df = spark_session.createDataFrame(
        [
            ('1', 'z',  1990, 2000, 'a', 'w'),
            ('1', 'y',  1990, 2000, 'b', 'z'),
            ('1', 'x',  1780, 1800, 'b', 'e'),
            ('1', 't',  1810, 2000, 'd', 'asd'),
        ],
        ['nconst', 'primaryName', 'birthYear', 'deathYear', 'primaryProfession', 'knownForTitles']
    )
    df_soundtrack= find_the_oldest_soundtrack(test_df)
    assert df_soundtrack == None
