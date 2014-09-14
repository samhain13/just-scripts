#! /usr/bin/env python
"""
    Generates a Lorem Ipsum article.
"""
from random import randint, sample
from sys import stdout

words = ["a", "ac", "accumsan", "adipiscing", "aenean", "aliquam", "aliquet",
"amet", "ante", "arcu", "at", "auctor", "augue", "bibendum", "blandit",
"commodo", "condimentum", "congue", "consectetur", "consequat", "convallis",
"cras", "cubilia", "curabitur", "cursus", "dapibus", "diam", "dictum",
"dictumst", "dignissim", "dolor", "donec", "dui", "duis", "efficitur",
"egestas", "eget", "eleifend", "elementum", "elit", "enim", "erat", "eros",
"est", "et", "etiam", "eu", "euismod", "ex", "facilisi", "facilisis", "fames",
"faucibus", "felis", "fermentum", "feugiat", "finibus", "fringilla", "fusce",
"gravida", "habitant", "habitasse", "hac", "hendrerit", "iaculis", "id",
"imperdiet", "in", "integer", "interdum", "ipsum", "justo", "lacinia", "lacus",
"laoreet", "lectus", "leo", "libero", "ligula", "lobortis", "lorem", "luctus",
"maecenas", "magna", "malesuada", "massa", "mattis", "mauris", "maximus",
"metus", "mi", "molestie", "mollis", "morbi", "nam", "nec", "neque", "netus",
"nibh", "nisi", "nisl", "non", "nulla", "nullam", "nunc", "odio", "orci",
"ornare", "pellentesque", "pharetra", "phasellus", "placerat", "platea", "porta",
"porttitor", "posuere", "potenti", "praesent", "pretium", "primis", "proin",
"pulvinar", "purus", "quam", "quis", "quisque", "rhoncus", "risus", "rutrum",
"sagittis", "sapien", "scelerisque", "sed", "sem", "semper", "senectus", "sit",
"sodales", "sollicitudin", "suscipit", "suspendisse", "tellus", "tempor",
"tempus", "tincidunt", "tortor", "tristique", "turpis", "ullamcorper",
"ultrices", "ultricies", "urna", "ut", "varius", "vehicula", "vel", "velit",
"venenatis", "vestibulum", "vitae", "vivamus", "viverra", "volutpat",
"vulputate"]

def make_sentence():
    sentence = sample(words, randint(3, 12))
    sentence[0] = sentence[0].title()
    return " ".join(sentence) + "."

def make_paragraph():
    sentences = [make_sentence() for x in xrange(randint(1, 5))]
    return " ".join(sentences)

def make_article():
    paragraphs = [make_paragraph() for x in xrange(randint(3, 10))]
    return "\n\n".join(paragraphs)

stdout.write("\n" + make_article() + "\n\n")

