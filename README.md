# AIML Movie Recommendation Bot a.k.a Popcorn

## Overview
**Popcorn** is designed to provide users with personalized movie recommendations based on various criteria. It can suggest movies by genre, actors, similar movies, mood. Unfortunately It cannot combine categories. Additionally, the bot can share interesting movie facts or provide random recommendations.

---

## Features
- **Movie Recommendations**
  - By Genre: Suggests movies from a specified genre.
  - By Actor/Actress: Recommends movies featuring a specific actor or actress. (using normalized names)
  - By Similar Movies: Provides recommendations based on a movie the user already likes. (can recommending the same movie as provided)
  - By Mood: Suggests movies that match a user's mood (mapped to genre -> mapped to movie).
  - Random Picks: Gives a random movie recommendation from a small selection.

- **Movie Facts**
  - Shares trivia or interesting facts about movies, directors, actors, or production details.

- **Remembering**
  - The bot can remember previous answers given and relay them again.


## Usage

### Example Conversations
#### 1. Recommendation by Genre
**User**: Recommend a *comedy* movie.  
**Bot**: Great choice! Here is a *Comedy* movie I recommend: The *Grand Budapest Hotel*, starring *Tony Revolori*. Would you like a suggestion from a different genre?

#### 2. Recommendation by Actor
**User**: Recommend something with *Tom Hanks*.  
**Bot**: They're a great actor indeed. Here's a movie featuring *Tom Hanks* that I recommend: *Cast Away*, This movie is a *Drama* film. Would you like a suggestion for a different actor?

#### 3. Recommendation by Similar Movie
**User**: I loved *Interstellar*. What should I watch next?  
**Bot**: Ah, *Interstellar* is a good movie. The lead actor of this movie is *Mackenzie Foy*. Here is a film with the same genre: *Inception*. Do you like any other movies?

#### 4. Recommendation by Mood
**User**: i'm *bored* please recommend something.  
**Bot**: Ah, so you’re feeling *bored*. How about watching a *drama* movie? Here's a recommendation for you: *The Shawshank Redemption*. The lead actor in this movie is: *Clancy Brown*. Can I make another recommandation, random this time?

#### 5. Random Recommendation
**User**: Surprise me with a movie suggestion.  
**Bot**: Here’s a must-watch movie for you! It’s titled "*Twilight*". A Romance masterpiece. Featuring the incredible talent of *Billy Burke*. Would You like another random recommendation?

#### 6. Movie Fact
**User**: Tell me an interesting fact.  
**Bot**: Of course! Hope you enjoy this one. After Alan Rickman was cast in “Harry Potter and the Philosopher’s Stone,” J.K. Rowling revealed to him how Severus Snape's story ended. Would you like to get another fact

---

## Configuration

### Required Data
The bot relies on a too small movie database with details such as:
- **Sets**:
  - Genres
  - Actors/Actresses
  - Mood tags
  - Movie Titles
- **Maps**:
  - Genres <-> Movie
  - Actors/Actresses <-> Movie
  - Moods -> Genre
- **Facts**: A list of trivia and facts about movies, actors, and directors. (within a random tag)
