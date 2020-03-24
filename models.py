# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Boardgames(models.Model):
    row_names = models.IntegerField(blank=True, null=True)
    game_id = models.IntegerField(db_column='game.id', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    game_type = models.TextField(db_column='game.type', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_description = models.TextField(db_column='details.description', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_image = models.TextField(db_column='details.image', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_maxplayers = models.IntegerField(db_column='details.maxplayers', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_maxplaytime = models.IntegerField(db_column='details.maxplaytime', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_minage = models.IntegerField(db_column='details.minage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_minplayers = models.IntegerField(db_column='details.minplayers', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_minplaytime = models.IntegerField(db_column='details.minplaytime', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_name = models.TextField(db_column='details.name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_playingtime = models.IntegerField(db_column='details.playingtime', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_thumbnail = models.TextField(db_column='details.thumbnail', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    details_yearpublished = models.IntegerField(db_column='details.yearpublished', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    attributes_boardgameartist = models.TextField(db_column='attributes.boardgameartist', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    attributes_boardgamecategory = models.TextField(db_column='attributes.boardgamecategory', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    attributes_boardgamecompilation = models.TextField(db_column='attributes.boardgamecompilation', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    attributes_boardgamedesigner = models.TextField(db_column='attributes.boardgamedesigner', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    attributes_boardgameexpansion = models.TextField(db_column='attributes.boardgameexpansion', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    attributes_boardgamefamily = models.TextField(db_column='attributes.boardgamefamily', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    attributes_boardgameimplementation = models.TextField(db_column='attributes.boardgameimplementation', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    attributes_boardgameintegration = models.TextField(db_column='attributes.boardgameintegration', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    attributes_boardgamemechanic = models.TextField(db_column='attributes.boardgamemechanic', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    attributes_boardgamepublisher = models.TextField(db_column='attributes.boardgamepublisher', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    attributes_total = models.FloatField(db_column='attributes.total', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_average = models.FloatField(db_column='stats.average', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_averageweight = models.FloatField(db_column='stats.averageweight', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_bayesaverage = models.FloatField(db_column='stats.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_abstracts_bayesaverage = models.TextField(db_column='stats.family.abstracts.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_abstracts_pos = models.TextField(db_column='stats.family.abstracts.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_cgs_bayesaverage = models.TextField(db_column='stats.family.cgs.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_cgs_pos = models.TextField(db_column='stats.family.cgs.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_childrensgames_bayesaverage = models.TextField(db_column='stats.family.childrensgames.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_childrensgames_pos = models.TextField(db_column='stats.family.childrensgames.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_familygames_bayesaverage = models.TextField(db_column='stats.family.familygames.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_familygames_pos = models.TextField(db_column='stats.family.familygames.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_partygames_bayesaverage = models.TextField(db_column='stats.family.partygames.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_partygames_pos = models.TextField(db_column='stats.family.partygames.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_strategygames_bayesaverage = models.TextField(db_column='stats.family.strategygames.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_strategygames_pos = models.TextField(db_column='stats.family.strategygames.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_thematic_bayesaverage = models.TextField(db_column='stats.family.thematic.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_thematic_pos = models.TextField(db_column='stats.family.thematic.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_wargames_bayesaverage = models.TextField(db_column='stats.family.wargames.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_wargames_pos = models.TextField(db_column='stats.family.wargames.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_median = models.FloatField(db_column='stats.median', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_numcomments = models.FloatField(db_column='stats.numcomments', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_numweights = models.FloatField(db_column='stats.numweights', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_owned = models.FloatField(db_column='stats.owned', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_stddev = models.FloatField(db_column='stats.stddev', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_subtype_boardgame_bayesaverage = models.FloatField(db_column='stats.subtype.boardgame.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_subtype_boardgame_pos = models.FloatField(db_column='stats.subtype.boardgame.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_trading = models.FloatField(db_column='stats.trading', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_usersrated = models.FloatField(db_column='stats.usersrated', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_wanting = models.FloatField(db_column='stats.wanting', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_wishing = models.FloatField(db_column='stats.wishing', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polls_language_dependence = models.TextField(db_column='polls.language_dependence', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polls_suggested_numplayers_1 = models.TextField(db_column='polls.suggested_numplayers.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polls_suggested_numplayers_10 = models.TextField(db_column='polls.suggested_numplayers.10', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polls_suggested_numplayers_2 = models.TextField(db_column='polls.suggested_numplayers.2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polls_suggested_numplayers_3 = models.TextField(db_column='polls.suggested_numplayers.3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polls_suggested_numplayers_4 = models.TextField(db_column='polls.suggested_numplayers.4', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polls_suggested_numplayers_5 = models.TextField(db_column='polls.suggested_numplayers.5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polls_suggested_numplayers_6 = models.TextField(db_column='polls.suggested_numplayers.6', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polls_suggested_numplayers_7 = models.TextField(db_column='polls.suggested_numplayers.7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polls_suggested_numplayers_8 = models.TextField(db_column='polls.suggested_numplayers.8', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polls_suggested_numplayers_9 = models.TextField(db_column='polls.suggested_numplayers.9', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polls_suggested_numplayers_over = models.TextField(db_column='polls.suggested_numplayers.Over', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    polls_suggested_playerage = models.TextField(db_column='polls.suggested_playerage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    attributes_t_links_concat_2_field = models.TextField(db_column='attributes.t.links.concat.2....', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    stats_family_amiga_bayesaverage = models.TextField(db_column='stats.family.amiga.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_amiga_pos = models.TextField(db_column='stats.family.amiga.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_arcade_bayesaverage = models.TextField(db_column='stats.family.arcade.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_arcade_pos = models.TextField(db_column='stats.family.arcade.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_atarist_bayesaverage = models.TextField(db_column='stats.family.atarist.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_atarist_pos = models.TextField(db_column='stats.family.atarist.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_commodore64_bayesaverage = models.TextField(db_column='stats.family.commodore64.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_family_commodore64_pos = models.TextField(db_column='stats.family.commodore64.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_subtype_rpgitem_bayesaverage = models.TextField(db_column='stats.subtype.rpgitem.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_subtype_rpgitem_pos = models.TextField(db_column='stats.subtype.rpgitem.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_subtype_videogame_bayesaverage = models.TextField(db_column='stats.subtype.videogame.bayesaverage', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    stats_subtype_videogame_pos = models.TextField(db_column='stats.subtype.videogame.pos', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'BoardGames'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    name = models.CharField(max_length=50)
    domain = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'django_site'


class ForumAttachmentsAttachment(models.Model):
    comment = models.CharField(max_length=255, blank=True, null=True)
    post = models.ForeignKey('ForumConversationPost', models.DO_NOTHING)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'forum_attachments_attachment'


class ForumConversationPost(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    subject = models.CharField(max_length=255)
    content = models.TextField()
    username = models.CharField(max_length=155, blank=True, null=True)
    approved = models.BooleanField()
    update_reason = models.CharField(max_length=255, blank=True, null=True)
    updates_count = models.PositiveIntegerField()
    field_content_rendered = models.TextField(db_column='_content_rendered', blank=True, null=True)  # Field renamed because it started with '_'.
    poster = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    topic = models.ForeignKey('ForumConversationTopic', models.DO_NOTHING)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    anonymous_key = models.CharField(max_length=100, blank=True, null=True)
    enable_signature = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'forum_conversation_post'


class ForumConversationTopic(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    subject = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    type = models.PositiveSmallIntegerField()
    status = models.PositiveIntegerField()
    approved = models.BooleanField()
    posts_count = models.PositiveIntegerField()
    views_count = models.PositiveIntegerField()
    last_post_on = models.DateTimeField(blank=True, null=True)
    forum = models.ForeignKey('ForumForum', models.DO_NOTHING)
    poster = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    first_post = models.ForeignKey(ForumConversationPost, models.DO_NOTHING, blank=True, null=True)
    last_post = models.ForeignKey(ForumConversationPost, models.DO_NOTHING, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forum_conversation_topic'


class ForumConversationTopicSubscribers(models.Model):
    topic = models.ForeignKey(ForumConversationTopic, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'forum_conversation_topic_subscribers'
        unique_together = (('topic', 'user'),)


class ForumForum(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    link_redirects = models.BooleanField()
    type = models.PositiveSmallIntegerField()
    link_redirects_count = models.PositiveIntegerField()
    last_post_on = models.DateTimeField(blank=True, null=True)
    display_sub_forum_list = models.BooleanField()
    field_description_rendered = models.TextField(db_column='_description_rendered', blank=True, null=True)  # Field renamed because it started with '_'.
    lft = models.PositiveIntegerField()
    tree_id = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    direct_posts_count = models.PositiveIntegerField()
    direct_topics_count = models.PositiveIntegerField()
    last_post = models.ForeignKey(ForumConversationPost, models.DO_NOTHING, blank=True, null=True)
    rght = models.PositiveIntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forum_forum'


class ForumMemberForumprofile(models.Model):
    signature = models.TextField(blank=True, null=True)
    posts_count = models.PositiveIntegerField()
    field_signature_rendered = models.TextField(db_column='_signature_rendered', blank=True, null=True)  # Field renamed because it started with '_'.
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forum_member_forumprofile'


class ForumPermissionForumpermission(models.Model):
    codename = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'forum_permission_forumpermission'


class ForumPermissionGroupforumpermission(models.Model):
    forum = models.ForeignKey(ForumForum, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey(ForumPermissionForumpermission, models.DO_NOTHING)
    has_perm = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'forum_permission_groupforumpermission'
        unique_together = (('permission', 'forum', 'group'),)


class ForumPermissionUserforumpermission(models.Model):
    anonymous_user = models.BooleanField()
    forum = models.ForeignKey(ForumForum, models.DO_NOTHING, blank=True, null=True)
    permission = models.ForeignKey(ForumPermissionForumpermission, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    has_perm = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'forum_permission_userforumpermission'
        unique_together = (('permission', 'forum', 'user'),)


class ForumPollsTopicpoll(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    question = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(blank=True, null=True)
    max_options = models.PositiveSmallIntegerField()
    user_changes = models.BooleanField()
    topic = models.ForeignKey(ForumConversationTopic, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'forum_polls_topicpoll'


class ForumPollsTopicpolloption(models.Model):
    text = models.CharField(max_length=255)
    poll = models.ForeignKey(ForumPollsTopicpoll, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'forum_polls_topicpolloption'


class ForumPollsTopicpollvote(models.Model):
    timestamp = models.DateTimeField()
    poll_option = models.ForeignKey(ForumPollsTopicpolloption, models.DO_NOTHING)
    anonymous_key = models.CharField(max_length=100, blank=True, null=True)
    voter = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forum_polls_topicpollvote'


class ForumTrackingForumreadtrack(models.Model):
    forum = models.ForeignKey(ForumForum, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    mark_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'forum_tracking_forumreadtrack'
        unique_together = (('user', 'forum'),)


class ForumTrackingTopicreadtrack(models.Model):
    topic = models.ForeignKey(ForumConversationTopic, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    mark_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'forum_tracking_topicreadtrack'
        unique_together = (('user', 'topic'),)
