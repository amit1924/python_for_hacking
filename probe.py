import requests


def urls(input_file, output_file):
    # Open the input file and read URLs from it
    with open(input_file, "r") as file:
        urls = file.read().splitlines()

    good_urls = []
    bad_urls = []

    # Iterate through each URL
    for url in urls:
        try:
            # Send a HEAD request to check the URL
            response = requests.head(url)

            # If the response status code is 200, the URL is considered good
            if response.status_code == 200:
                good_urls.append(url)
            else:
                # Otherwise, the URL is considered bad
                bad_urls.append(url)

        # Handle the case where an invalid URL schema is encountered
        except requests.exceptions.MissingSchema:
            bad_urls.append(url)
            continue

    # Write the filtered good URLs to the output file
    with open(output_file, "w") as file:
        # Write each good URL on a new line
        file.write("\n".join(good_urls))

    # Print the name of the output file to indicate where the URLs are saved
    print(f"Saved good URLs in: {output_file}")


input_file = "urls.txt"
output_file = "filtered_urls.txt"
urls(input_file, output_file)
