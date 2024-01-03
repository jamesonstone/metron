import csv
import argparse
import csv
import argparse
import webbrowser
from data_prep import prep
from rag.gen import init_langchain, prompt


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--load", action="store_true", help="pre-load data leveraging yelp fusion api"
    )
    args = parser.parse_args()

    if args.load:
        prep.run()
    else:
        pass
        agent = init_langchain()
        try:
            while True:
                question = input("🤖 Please enter your question: ")
                prompt(agent, question)
        except KeyboardInterrupt:
            pass


def render_html():
    html = """
    <html>
    <head>
    <style>
    .center {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    </style>
    </head>
    <body>
    <div class="center">
    <h1>How many businesses are there?</h1>
    </div>
    </body>
    </html>
    """
    return html


### MAIN ###
if __name__ == "__main__":
    run()

    #
    # TODO: render Website and place question prompt in table
    #
    # rendered_html = render_html()
    # print(rendered_html)
    # with open('./html/output.html', 'w') as file:
    #   file.write(rendered_html)
    # webbrowser.open('output.html')
    # print("If you browser does not open, please run the following command: open ./html/output.html")
