import logging
from . import movie
LOGGER = logging.getLogger(__name__)


def main() -> None:
    spark = movie.get_spark()
    df = movie.read_data(spark)
    oldest = movie.find_the_oldest_soundtrack(df)
    LOGGER.info(f"Oldest soundtrack is {oldest}.")


if __name__ == "__main__":
    main()
