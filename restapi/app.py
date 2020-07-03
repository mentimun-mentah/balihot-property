from services.serve import app, api
from services.resources import (
    Users,
    Regions,
    Teams,
    Facilities,
    Properties,
    Types
)
from services.libs import OAuth2

api.add_resource(Users.RegisterUser,'/register')
api.add_resource(Users.ConfirmEmail,'/user-confirm/<token>',endpoint='user.confirm')
api.add_resource(Users.ResendEmail,'/resend-email')
api.add_resource(Users.LoginUser,'/login')
api.add_resource(Users.RefreshToken,'/refresh')
api.add_resource(Users.AccessTokenRevoke,'/access_revoke')
api.add_resource(Users.RefreshTokenRevoke,'/refresh_revoke')
api.add_resource(Users.SendPasswordReset,'/send-password/reset')
api.add_resource(Users.ResetPassword,'/password/reset/<token>',endpoint='user.reset_password')

api.add_resource(OAuth2.GoogleLogin,'/login/google')
api.add_resource(OAuth2.GoogleAuthorize,'/login/google/authorized')
api.add_resource(OAuth2.FacebookLogin,'/login/facebook')
api.add_resource(OAuth2.FacebookAuthorize,'/login/facebook/authorized')

api.add_resource(Users.AddPassword,'/account/add-password')
api.add_resource(Users.UpdatePassword,'/account/update-password')
api.add_resource(Users.UpdateAvatar,'/account/update-avatar')
api.add_resource(Users.UpdateAccount,'/account/update-account')

api.add_resource(Regions.AllRegion,'/regions')
api.add_resource(Regions.CreateRegion,'/region/create')
api.add_resource(Regions.GetUpdateDeleteRegion,'/region/crud/<int:id>')

api.add_resource(Teams.AllTeam,'/teams')
api.add_resource(Teams.CreateTeam,'/team/create')
api.add_resource(Teams.GetUpdateDeleteTeam,'/team/crud/<int:id>')

api.add_resource(Facilities.AllFacility,'/facilities')
api.add_resource(Facilities.CreateFacility,'/facility/create')
api.add_resource(Facilities.GetUpdateDeleteFacility,'/facility/crud/<int:id>')

api.add_resource(Types.AllType,'/types')

api.add_resource(Properties.CreateProperty,'/property/create')
api.add_resource(Properties.GetUpdateDeleteProperty,'/property/crud/<int:id>')
api.add_resource(Properties.DeleteImageProperty,'/property/delete-images/<int:id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
