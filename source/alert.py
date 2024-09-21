from argparse import ArgumentParser
from mailer import send_email


def setup_args(parser):
    """A function that builds the parser to read command-line input

    Args:
        parser (_type_): A parser object from the ArgumentParser Package

    Returns:
        _type_: A parsers with arguments for sender (str), recipient (str), subject (str), and body (str) to build the email to be sent with the mailer class
    """
    parser.add_argument("-s", "--sender", type=str, required=True)
    parser.add_argument("-r", "--recipient", type=str, required=True)
    parser.add_argument("-j", "--subject", type=str, default="Subject")
    parser.add_argument("-b", "--body", type=str, default="Body")
    return parser

def main():
    """Parse command line input and send it to the email delivery function
    """
    parser = ArgumentParser()
    args = setup_args(parser).parse_args()

    send_email(
        sender=args.sender,
        recipient=args.recipient,
        subject=args.subject,
        body=args.body
    )

if __name__ == "__main__":
    main()