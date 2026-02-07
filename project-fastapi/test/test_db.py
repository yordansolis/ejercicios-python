from main import DBHero


def test_create_hero_in_db(db_session):
    hero = DBHero(name="Bruce Wayne", secret_name="Batman", age=35)
    db_session.add(hero)
    db_session.commit()
    db_session.refresh(hero)

    assert hero.id is not None
    assert hero.name == "Bruce Wayne"
    assert hero.secret_name == "Batman"
    assert hero.age == 35


def test_query_heroes(db_session):
    hero = DBHero(name="Clark Kent", secret_name="Superman", age=30)
    db_session.add(hero)
    db_session.commit()

    result = db_session.query(DBHero).filter_by(name="Clark Kent").first()
    assert result is not None
    assert result.secret_name == "Superman"
