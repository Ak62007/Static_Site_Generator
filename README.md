# Static Site Generator

This is a custom-built static site generator written in Python. It converts raw Markdown files into a fully styled HTML website using a template-based system.

## Features

* **Markdown to HTML**: Converts Markdown elements like headings, lists, code blocks, and quotes into HTML.
* **Recursive Generation**: Automatically traverses the `content` directory to build a matching structure in the `docs` folder.
* **Asset Management**: Synchronizes static assets like images and CSS files to the final build directory.
* **Custom Styling**: Uses a dedicated CSS file to provide a consistent, themed look across the site.

## Project Structure

* **`src/`**: Contains the Python source code for parsing Markdown and generating HTML.
* **`content/`**: Place your raw Markdown (`.md`) files here.
* **`static/`**: Store your images and CSS files here.
* **`template.html`**: The base HTML shell used to wrap your content.
* **`docs/`**: The output directory where the final website is generated.

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Building the Site

To generate your website, run the following command from the root directory:

```bash
sh main.sh

```

This script will build the site and start a local development server at `http://localhost:8888`.

### Running Tests

To ensure everything is working correctly, you can run the included unit tests:

```bash
sh test.sh

```

This will discover and execute all tests located in the `src/` directory.

## How It Works

1. The generator clears the `docs/` folder and copies all files from `static/` into it.
2. It recursively scans the `content/` folder for `.md` files.
3. Each Markdown file is parsed into HTML nodes, injected into `template.html`, and saved as an `.html` file in the `docs/` folder.
