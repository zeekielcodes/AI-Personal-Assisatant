import random

def advice():
    quotes = [
        "The unexamined life is not worth living. - Socrates",
        "The only true journey is the one within. - Rainer Maria Rilke",
        "Our greatest glory consists not in never falling, but in rising every time we fall. - Nelson Mandela",
        "Be the change you wish to see in the world. - Mahatma Gandhi",
        "The difference between successful people and others is not a lack of strength, not a lack of knowledge, but rather a lack of will. - Vince Lombardi",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",

        "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. - Albert Einstein",
        "The mind is everything. What you think you become. - Buddha",
        "The only regret in life is the life you could have lived. - Pablo Picasso",
        "A journey of a thousand miles begins with a single step. - Lao Tzu",
        "Don't worry, be happy. - Bobby McFerrin",
        "The best way to predict the future is to create it. - Peter Drucker",
        "Curiosity is the key to creativity. - Leo Burnett",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "The Earth has music for those who listen. - William Shakespeare",
        "A flower does not think of competing with the flower next to it. It just blooms. - Zen Shin",
        "To love and be loved is to feel the sun from both sides. - David Viscott",
        "The greatest happiness in the world is to know you are loved for what you are, or in spite of what you are. - Victor Hugo",
        "There is only one happiness in this life, to love and be loved. - George Sand",
        "A successful marriage requires falling in love many times, always with the same person. - Mignon McLaughlin",
        "Love is friendship that has caught fire. - Ann Landers",
        "A man who laughs at himself laughs at nothing that is really funny. - George Bernard Shaw",
        "The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle. - Steve Jobs",
        "The difference between ordinary and extraordinary is that little extra. - Jimmy Johnson",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",

        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",

        "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. - Albert Einstein",
        "The mind is everything. What you think you become. - Buddha",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "The best way to predict the future is to create it. - Peter Drucker",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "It is never too late to be what you might have been. - George Eliot",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Don't cry because it's over, smile because it happened. - Dr. Seuss",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "Life is really simple, but we insist on making it complicated. - Confucius",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. - Buddha",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "The best way to predict the future is to create it. - Peter Drucker",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "It is never too late to be what you might have been. - George Eliot",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Don't cry because it's over, smile because it happened. - Dr. Seuss",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "Life is really simple, but we insist on making it complicated. - Confucius",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. - Buddha",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "The best way to predict the future is to create it. - Peter Drucker",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "It is never too late to be what you might have been. - George Eliot",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Don't cry because it's over, smile because it happened. - Dr. Seuss",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "Life is really simple, but we insist on making it complicated. - Confucius",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. - Buddha",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "The best way to predict the future is to create it. - Peter Drucker",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "It is never too late to be what you might have been. - George Eliot",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Don't cry because it's over, smile because it happened. - Dr. Seuss",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "Life is really simple, but we insist on making it complicated. - Confucius",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. - Buddha",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "The best way to predict the future is to create it. - Peter Drucker",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "It is never too late to be what you might have been. - George Eliot",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Don't cry because it's over, smile because it happened. - Dr. Seuss",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "Life is really simple, but we insist on making it complicated. - Confucius",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. - Buddha",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "The best way to predict the future is to create it. - Peter Drucker",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "It is never too late to be what you might have been. - George Eliot",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Don't cry because it's over, smile because it happened. - Dr. Seuss",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "Life is really simple, but we insist on making it complicated. - Confucius",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. - Buddha",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "The best way to predict the future is to create it. - Peter Drucker",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "It is never too late to be what you might have been. - George Eliot",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Don't cry because it's over, smile because it happened. - Dr. Seuss",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "Life is really simple, but we insist on making it complicated. - Confucius",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. - Buddha",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "The best way to predict the future is to create it. - Peter Drucker",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    ]

    random_quote = random.choice(quotes)
    return random_quote